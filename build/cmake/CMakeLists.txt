CMAKE_MINIMUM_REQUIRED(VERSION 3.2)
PROJECT(${CFG_PROJECT_NAME})

STRING(TOUPPER ${CFG_PROJECT_NAME} CFG_PROJECT_NAME_UPPER)
SET(MAKER_PATH ../../${CFG_DEPENDENT_PATH}/maker)
INCLUDE(${MAKER_PATH}/maker.cmake)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${NO_RTTI_FLAG}")

INCLUDE_DIRECTORIES(${PROJECT_BINARY_DIR} ../../${CFG_INCLUDE_PATH})
ADD_DEFINITIONS(-DBUILD_ARCH_${BUILD_ARCH} -DBUILD_PLATFORM_${BUILD_PLATFORM})

LIST(APPEND LIB_FILE_PATHS ${INCLUDE_PATH})
LIST(APPEND LIB_FILE_PATHS ${SOURCE_PATH})
SEARCH_FILES(LIB_FILE_LIST ${CFG_PROJECT_NAME} LIB_FILE_PATHS)
ADD_LIBRARY(${CFG_PROJECT_NAME}_static STATIC ${LIB_FILE_LIST})
ADD_LIBRARY(${CFG_PROJECT_NAME}_shared SHARED ${LIB_FILE_LIST})
TARGET_COMPILE_DEFINITIONS(${CFG_PROJECT_NAME}_static PRIVATE BUILD_STATIC_LIB)
TARGET_COMPILE_DEFINITIONS(${CFG_PROJECT_NAME}_shared PRIVATE BUILD_SHARED_LIB ${CFG_PROJECT_NAME_UPPER}_EXPORTS)

SUBDIRLIST(TEST_LIST ${TEST_PATH})
FOREACH(ITER ${TEST_LIST})
	UNSET(TEST_FILE_PATH)
	LIST(APPEND TEST_FILE_PATH ${TEST_PATH}/${ITER})
	SEARCH_FILES(TEST_FILE_LIST ${ITER} TEST_FILE_PATH)
	ADD_EXECUTABLE(${ITER}_static ${TEST_FILE_LIST})
	ADD_EXECUTABLE(${ITER}_shared ${TEST_FILE_LIST})
	TARGET_COMPILE_DEFINITIONS(${ITER}_static PRIVATE BUILD_STATIC_LIB)
	TARGET_COMPILE_DEFINITIONS(${ITER}_shared PRIVATE BUILD_SHARED_LIB)
	TARGET_LINK_LIBRARIES(${ITER}_static ${CFG_PROJECT_NAME}_static)
	TARGET_LINK_LIBRARIES(${ITER}_shared ${CFG_PROJECT_NAME}_shared)
ENDFOREACH()
