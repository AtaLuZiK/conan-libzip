import os

from conans import ConanFile, CMake, tools


class LibzipConan(ConanFile):
    name = "libzip"
    version = "1.5.1"
    license = "https://github.com/nih-at/libzip/blob/master/LICENSE"
    url = "https://github.com/AtaLuZiK/conan-libzip"
    description = "A C library for reading, creating, and modifying zip archives."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    requires = "zlib/1.2.11@conan/stable"
    exports_sources = "libzip-config.cmake"
    generators = "cmake"

    @property
    def zip_folder_name(self):
        return "libzip-%s" % self.version

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        zip_name = self.zip_folder_name + ".tar.gz"
        tools.download("https://libzip.org/download/" + zip_name, zip_name)
        tools.check_md5(zip_name, "ca72a4c93bef1595e5ff45eaf534d4da")
        tools.unzip(zip_name)
        os.unlink(zip_name)

        with tools.chdir(self.zip_folder_name):
            tools.replace_in_file("CMakeLists.txt", "PROJECT(libzip C)", '''PROJECT(libzip C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')
            tools.replace_in_file("CMakeLists.txt", "ADD_SUBDIRECTORY(man)", "")
            tools.replace_in_file("CMakeLists.txt", "ADD_SUBDIRECTORY(regress)", "")
            tools.replace_in_file("CMakeLists.txt", "ADD_SUBDIRECTORY(examples)", "")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_GNUTLS"] = "OFF"
        cmake.definitions["ENABLE_OPENSSL"] = "OFF"
        cmake.definitions["ENABLE_COMMONCRYPTO"] = "OFF"
        cmake.configure(source_folder=self.zip_folder_name)
        cmake.build()

    def package(self):
        self.copy("zipconf.h", dst="include")
        self.copy("zip.h", dst="include", src=os.path.join(self.zip_folder_name, "lib"))
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("zip.dll", dst="bin", keep_path=False)
        self.copy("libzip-config.cmake", dst=".")

    def package_info(self):
        self.cpp_info.libs = ["zip"]

