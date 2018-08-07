find_path(LIBZIP_INCLUDE_DIR NAMES zip.h zipconf.h PATHS ${CONAN_INCLUDE_DIRS_LIBZIP})
find_library(LIBZIP_LIBRARY NAMES zip PATHS ${CONAN_LIB_DIRS_LIBZIP})

find_package(ZLIB REQUIRED)

add_library(libzip INTERFACE IMPORTED)
target_include_directories(libzip
  INTERFACE ${LIBZIP_INCLUDE_DIR}
  INTERFACE ${ZLIB_INCLUDE_DIR}
)
target_link_libraries(libzip
  INTERFACE ${LIBZIP_LIBRARY}
  INTERFACE ${ZLIB_LIBRARY}
)

mark_as_advanced(LIBZIP_INCLUDE_DIR LIBZIP_LIBRARY_DIR LIBZIP_LIBRARY)

message("** libzip found by Conan!")
set(LIBZIP_FOUND TRUE)
message("   - includes: ${LIBZIP_INCLUDE_DIR}")
message("   - libraries: ${LIBZIP_LIBRARY}")
