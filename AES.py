import math

multiplication_by_2 = [
    [0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e],
    [0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e],
    [0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e],
    [0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e],
    [0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e],
    [0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe],
    [0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde],
    [0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe],
    [0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05],
    [0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25],
    [0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45],
    [0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65],
    [0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85],
    [0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5],
    [0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5],
    [0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5]
]
multiplication_by_3 = [
    [0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11],
    [0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21],
    [0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71],
    [0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41],
    [0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1],
    [0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1],
    [0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1],
    [0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81],
    [0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a],
    [0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba],
    [0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea],
    [0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda],
    [0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a],
    [0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a],
    [0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a],
    [0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a]
]
multiplication_by_9 = [
    [0x00, 0x09, 0x12, 0x1b, 0x24, 0x2d, 0x36, 0x3f, 0x48, 0x41, 0x5a, 0x53, 0x6c, 0x65, 0x7e, 0x77],
    [0x90, 0x99, 0x82, 0x8b, 0xb4, 0xbd, 0xa6, 0xaf, 0xd8, 0xd1, 0xca, 0xc3, 0xfc, 0xf5, 0xee, 0xe7],
    [0x3b, 0x32, 0x29, 0x20, 0x1f, 0x16, 0x0d, 0x04, 0x73, 0x7a, 0x61, 0x68, 0x57, 0x5e, 0x45, 0x4c],
    [0xab, 0xa2, 0xb9, 0xb0, 0x8f, 0x86, 0x9d, 0x94, 0xe3, 0xea, 0xf1, 0xf8, 0xc7, 0xce, 0xd5, 0xdc],
    [0x76, 0x7f, 0x64, 0x6d, 0x52, 0x5b, 0x40, 0x49, 0x3e, 0x37, 0x2c, 0x25, 0x1a, 0x13, 0x08, 0x01],
    [0xe6, 0xef, 0xf4, 0xfd, 0xc2, 0xcb, 0xd0, 0xd9, 0xae, 0xa7, 0xbc, 0xb5, 0x8a, 0x83, 0x98, 0x91],
    [0x4d, 0x44, 0x5f, 0x56, 0x69, 0x60, 0x7b, 0x72, 0x05, 0x0c, 0x17, 0x1e, 0x21, 0x28, 0x33, 0x3a],
    [0xdd, 0xd4, 0xcf, 0xc6, 0xf9, 0xf0, 0xeb, 0xe2, 0x95, 0x9c, 0x87, 0x8e, 0xb1, 0xb8, 0xa3, 0xaa],
    [0xec, 0xe5, 0xfe, 0xf7, 0xc8, 0xc1, 0xda, 0xd3, 0xa4, 0xad, 0xb6, 0xbf, 0x80, 0x89, 0x92, 0x9b],
    [0x7c, 0x75, 0x6e, 0x67, 0x58, 0x51, 0x4a, 0x43, 0x34, 0x3d, 0x26, 0x2f, 0x10, 0x19, 0x02, 0x0b],
    [0xd7, 0xde, 0xc5, 0xcc, 0xf3, 0xfa, 0xe1, 0xe8, 0x9f, 0x96, 0x8d, 0x84, 0xbb, 0xb2, 0xa9, 0xa0],
    [0x47, 0x4e, 0x55, 0x5c, 0x63, 0x6a, 0x71, 0x78, 0x0f, 0x06, 0x1d, 0x14, 0x2b, 0x22, 0x39, 0x30],
    [0x9a, 0x93, 0x88, 0x81, 0xbe, 0xb7, 0xac, 0xa5, 0xd2, 0xdb, 0xc0, 0xc9, 0xf6, 0xff, 0xe4, 0xed],
    [0x0a, 0x03, 0x18, 0x11, 0x2e, 0x27, 0x3c, 0x35, 0x42, 0x4b, 0x50, 0x59, 0x66, 0x6f, 0x74, 0x7d],
    [0xa1, 0xa8, 0xb3, 0xba, 0x85, 0x8c, 0x97, 0x9e, 0xe9, 0xe0, 0xfb, 0xf2, 0xcd, 0xc4, 0xdf, 0xd6],
    [0x31, 0x38, 0x23, 0x2a, 0x15, 0x1c, 0x07, 0x0e, 0x79, 0x70, 0x6b, 0x62, 0x5d, 0x54, 0x4f, 0x46]
]
multiplication_by_11 = [
    [0x00, 0x0b, 0x16, 0x1d, 0x2c, 0x27, 0x3a, 0x31, 0x58, 0x53, 0x4e, 0x45, 0x74, 0x7f, 0x62, 0x69],
    [0xb0, 0xbb, 0xa6, 0xad, 0x9c, 0x97, 0x8a, 0x81, 0xe8, 0xe3, 0xfe, 0xf5, 0xc4, 0xcf, 0xd2, 0xd9],
    [0x7b, 0x70, 0x6d, 0x66, 0x57, 0x5c, 0x41, 0x4a, 0x23, 0x28, 0x35, 0x3e, 0x0f, 0x04, 0x19, 0x12],
    [0xcb, 0xc0, 0xdd, 0xd6, 0xe7, 0xec, 0xf1, 0xfa, 0x93, 0x98, 0x85, 0x8e, 0xbf, 0xb4, 0xa9, 0xa2],
    [0xf6, 0xfd, 0xe0, 0xeb, 0xda, 0xd1, 0xcc, 0xc7, 0xae, 0xa5, 0xb8, 0xb3, 0x82, 0x89, 0x94, 0x9f],
    [0x46, 0x4d, 0x50, 0x5b, 0x6a, 0x61, 0x7c, 0x77, 0x1e, 0x15, 0x08, 0x03, 0x32, 0x39, 0x24, 0x2f],
    [0x8d, 0x86, 0x9b, 0x90, 0xa1, 0xaa, 0xb7, 0xbc, 0xd5, 0xde, 0xc3, 0xc8, 0xf9, 0xf2, 0xef, 0xe4],
    [0x3d, 0x36, 0x2b, 0x20, 0x11, 0x1a, 0x07, 0x0c, 0x65, 0x6e, 0x73, 0x78, 0x49, 0x42, 0x5f, 0x54],
    [0xf7, 0xfc, 0xe1, 0xea, 0xdb, 0xd0, 0xcd, 0xc6, 0xaf, 0xa4, 0xb9, 0xb2, 0x83, 0x88, 0x95, 0x9e],
    [0x47, 0x4c, 0x51, 0x5a, 0x6b, 0x60, 0x7d, 0x76, 0x1f, 0x14, 0x09, 0x02, 0x33, 0x38, 0x25, 0x2e],
    [0x8c, 0x87, 0x9a, 0x91, 0xa0, 0xab, 0xb6, 0xbd, 0xd4, 0xdf, 0xc2, 0xc9, 0xf8, 0xf3, 0xee, 0xe5],
    [0x3c, 0x37, 0x2a, 0x21, 0x10, 0x1b, 0x06, 0x0d, 0x64, 0x6f, 0x72, 0x79, 0x48, 0x43, 0x5e, 0x55],
    [0x01, 0x0a, 0x17, 0x1c, 0x2d, 0x26, 0x3b, 0x30, 0x59, 0x52, 0x4f, 0x44, 0x75, 0x7e, 0x63, 0x68],
    [0xb1, 0xba, 0xa7, 0xac, 0x9d, 0x96, 0x8b, 0x80, 0xe9, 0xe2, 0xff, 0xf4, 0xc5, 0xce, 0xd3, 0xd8],
    [0x7a, 0x71, 0x6c, 0x67, 0x56, 0x5d, 0x40, 0x4b, 0x22, 0x29, 0x34, 0x3f, 0x0e, 0x05, 0x18, 0x13],
    [0xca, 0xc1, 0xdc, 0xd7, 0xe6, 0xed, 0xf0, 0xfb, 0x92, 0x99, 0x84, 0x8f, 0xbe, 0xb5, 0xa8, 0xa3]
]
multiplication_by_13 = [
    [0x00, 0x0d, 0x1a, 0x17, 0x34, 0x39, 0x2e, 0x23, 0x68, 0x65, 0x72, 0x7f, 0x5c, 0x51, 0x46, 0x4b],
    [0xd0, 0xdd, 0xca, 0xc7, 0xe4, 0xe9, 0xfe, 0xf3, 0xb8, 0xb5, 0xa2, 0xaf, 0x8c, 0x81, 0x96, 0x9b],
    [0xbb, 0xb6, 0xa1, 0xac, 0x8f, 0x82, 0x95, 0x98, 0xd3, 0xde, 0xc9, 0xc4, 0xe7, 0xea, 0xfd, 0xf0],
    [0x6b, 0x66, 0x71, 0x7c, 0x5f, 0x52, 0x45, 0x48, 0x03, 0x0e, 0x19, 0x14, 0x37, 0x3a, 0x2d, 0x20],
    [0x6d, 0x60, 0x77, 0x7a, 0x59, 0x54, 0x43, 0x4e, 0x05, 0x08, 0x1f, 0x12, 0x31, 0x3c, 0x2b, 0x26],
    [0xbd, 0xb0, 0xa7, 0xaa, 0x89, 0x84, 0x93, 0x9e, 0xd5, 0xd8, 0xcf, 0xc2, 0xe1, 0xec, 0xfb, 0xf6],
    [0xd6, 0xdb, 0xcc, 0xc1, 0xe2, 0xef, 0xf8, 0xf5, 0xbe, 0xb3, 0xa4, 0xa9, 0x8a, 0x87, 0x90, 0x9d],
    [0x06, 0x0b, 0x1c, 0x11, 0x32, 0x3f, 0x28, 0x25, 0x6e, 0x63, 0x74, 0x79, 0x5a, 0x57, 0x40, 0x4d],
    [0xda, 0xd7, 0xc0, 0xcd, 0xee, 0xe3, 0xf4, 0xf9, 0xb2, 0xbf, 0xa8, 0xa5, 0x86, 0x8b, 0x9c, 0x91],
    [0x0a, 0x07, 0x10, 0x1d, 0x3e, 0x33, 0x24, 0x29, 0x62, 0x6f, 0x78, 0x75, 0x56, 0x5b, 0x4c, 0x41],
    [0x61, 0x6c, 0x7b, 0x76, 0x55, 0x58, 0x4f, 0x42, 0x09, 0x04, 0x13, 0x1e, 0x3d, 0x30, 0x27, 0x2a],
    [0xb1, 0xbc, 0xab, 0xa6, 0x85, 0x88, 0x9f, 0x92, 0xd9, 0xd4, 0xc3, 0xce, 0xed, 0xe0, 0xf7, 0xfa],
    [0xb7, 0xba, 0xad, 0xa0, 0x83, 0x8e, 0x99, 0x94, 0xdf, 0xd2, 0xc5, 0xc8, 0xeb, 0xe6, 0xf1, 0xfc],
    [0x67, 0x6a, 0x7d, 0x70, 0x53, 0x5e, 0x49, 0x44, 0x0f, 0x02, 0x15, 0x18, 0x3b, 0x36, 0x21, 0x2c],
    [0x0c, 0x01, 0x16, 0x1b, 0x38, 0x35, 0x22, 0x2f, 0x64, 0x69, 0x7e, 0x73, 0x50, 0x5d, 0x4a, 0x47],
    [0xdc, 0xd1, 0xc6, 0xcb, 0xe8, 0xe5, 0xf2, 0xff, 0xb4, 0xb9, 0xae, 0xa3, 0x80, 0x8d, 0x9a, 0x97]
]
multiplication_by_14 = [
    [0x00, 0x0e, 0x1c, 0x12, 0x38, 0x36, 0x24, 0x2a, 0x70, 0x7e, 0x6c, 0x62, 0x48, 0x46, 0x54, 0x5a],
    [0xe0, 0xee, 0xfc, 0xf2, 0xd8, 0xd6, 0xc4, 0xca, 0x90, 0x9e, 0x8c, 0x82, 0xa8, 0xa6, 0xb4, 0xba],
    [0xdb, 0xd5, 0xc7, 0xc9, 0xe3, 0xed, 0xff, 0xf1, 0xab, 0xa5, 0xb7, 0xb9, 0x93, 0x9d, 0x8f, 0x81],
    [0x3b, 0x35, 0x27, 0x29, 0x03, 0x0d, 0x1f, 0x11, 0x4b, 0x45, 0x57, 0x59, 0x73, 0x7d, 0x6f, 0x61],
    [0xad, 0xa3, 0xb1, 0xbf, 0x95, 0x9b, 0x89, 0x87, 0xdd, 0xd3, 0xc1, 0xcf, 0xe5, 0xeb, 0xf9, 0xf7],
    [0x4d, 0x43, 0x51, 0x5f, 0x75, 0x7b, 0x69, 0x67, 0x3d, 0x33, 0x21, 0x2f, 0x05, 0x0b, 0x19, 0x17],
    [0x76, 0x78, 0x6a, 0x64, 0x4e, 0x40, 0x52, 0x5c, 0x06, 0x08, 0x1a, 0x14, 0x3e, 0x30, 0x22, 0x2c],
    [0x96, 0x98, 0x8a, 0x84, 0xae, 0xa0, 0xb2, 0xbc, 0xe6, 0xe8, 0xfa, 0xf4, 0xde, 0xd0, 0xc2, 0xcc],
    [0x41, 0x4f, 0x5d, 0x53, 0x79, 0x77, 0x65, 0x6b, 0x31, 0x3f, 0x2d, 0x23, 0x09, 0x07, 0x15, 0x1b],
    [0xa1, 0xaf, 0xbd, 0xb3, 0x99, 0x97, 0x85, 0x8b, 0xd1, 0xdf, 0xcd, 0xc3, 0xe9, 0xe7, 0xf5, 0xfb],
    [0x9a, 0x94, 0x86, 0x88, 0xa2, 0xac, 0xbe, 0xb0, 0xea, 0xe4, 0xf6, 0xf8, 0xd2, 0xdc, 0xce, 0xc0],
    [0x7a, 0x74, 0x66, 0x68, 0x42, 0x4c, 0x5e, 0x50, 0x0a, 0x04, 0x16, 0x18, 0x32, 0x3c, 0x2e, 0x20],
    [0xec, 0xe2, 0xf0, 0xfe, 0xd4, 0xda, 0xc8, 0xc6, 0x9c, 0x92, 0x80, 0x8e, 0xa4, 0xaa, 0xb8, 0xb6],
    [0x0c, 0x02, 0x10, 0x1e, 0x34, 0x3a, 0x28, 0x26, 0x7c, 0x72, 0x60, 0x6e, 0x44, 0x4a, 0x58, 0x56],
    [0x37, 0x39, 0x2b, 0x25, 0x0f, 0x01, 0x13, 0x1d, 0x47, 0x49, 0x5b, 0x55, 0x7f, 0x71, 0x63, 0x6d],
    [0xd7, 0xd9, 0xcb, 0xc5, 0xef, 0xe1, 0xf3, 0xfd, 0xa7, 0xa9, 0xbb, 0xb5, 0x9f, 0x91, 0x83, 0x8d]
]
sbox = [
    # 0     1     2     3      4     5     6     7     8    9     a      b    c     d      e     f
    ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],  # 0
    ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],  # 1
    ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],  # 2
    ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],  # 3
    ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],  # 4
    ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],  # 5
    ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],  # 6
    ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],  # 7
    ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],  # 8
    ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],  # 9
    ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],  # a
    ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],  # b
    ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],  # c
    ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],  # d
    ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],  # e
    ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']  # f
]
sboxInv = [
    # 0     1     2     3      4     5     6     7     8    9     a      b    c     d      e     f
    ['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],  # 0
    ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],  # 1
    ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],  # 2
    ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],  # 3
    ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],  # 4
    ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],  # 5
    ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],  # 6
    ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],  # 7
    ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],  # 8
    ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],  # 9
    ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],  # a
    ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],  # b
    ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],  # c
    ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],  # d
    ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],  # e
    ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']  # f
]


# for encryption
def getLists(message: str) -> list:
    """
    divide the message into 128 bits chunks and every chunk is
    represented as a list then converted to a matrix 4×4
    and all matrices of chunks are listed in one list

    return
    one list containing matrix 4×4 for every 128 bit
    """
    while len(message) % 16 != 0:
        message = message + ' '

    chunks_list, index = [], 0

    for j in range(math.ceil(len(message) / 16)):

        lis = []
        for i in range(index, index + 16):
            lis.append(message[i].encode('utf-8').hex())

        chunks_list.append(lis)
        index = index + 16

    matrices = []
    for lis in chunks_list:
        matrix = []
        start, end = 0, 3
        for i in range(0, 4):
            matrix.append(lis[start:end + 1])
            start = end + 1
            end = end + 4
        matrices.append(matrix)
    return matrices


def convertToMatrix(message: str) -> list:
    """
    use it to handle encrypted input from the user
    """
    matrices = []
    char = 0
    for matNum in range(int(len(message) / 32)):
        matrix = []
        for j in range(0, 4):
            newLis = []
            for i in range(0, 4):
                newLis.append(message[char:char + 2])
                char = char + 2
            matrix.append(newLis)
        matrices.append(matrix)

    return matrices


def inputKey(key: str) -> list:
    """
    take the key as a string of hexadecimal and convert it
    to a matrix 4×4 consists of 4 col every col is 4 bytes
    :param key: str
    :return:
    matrix (list of cols)
    """
    colList, matrix = [], []
    for i in range(0, len(key), 2):
        colList.append(key[i:i + 2])

        if len(colList) == 4:
            matrix.append(colList)
            colList = []

    return matrix


def reverseMatrix(state: list) -> list:
    """
    helping method to reverse a matrix
    rows become columns and
    columns become rows
    """
    newState = []
    for i in range(0, 4):
        newCol = []
        for j in range(0, 4):
            newCol.append(state[j][i])
        newState.append(newCol)
    return newState


def mult(num: str, by: int) -> str:
    """
    multiple in mix col operation
    """
    result = ''
    if by == 1:
        result = num
    if by == 2:
        result = multiplication_by_2[int(num[0], 16)][int(num[1], 16)]
        result = str(hex(result))
        if len(result) < 4:
            result = result[0:2] + '0' + result[2:]
        result = result[2:]
    if by == 3:
        result = multiplication_by_3[int(num[0], 16)][int(num[1], 16)]
        result = str(hex(result))
        if len(result) < 4:
            result = result[0:2] + '0' + result[2:]
        result = result[2:]
    if by == 9:
        result = multiplication_by_9[int(num[0], 16)][int(num[1], 16)]
        result = str(hex(result))
        if len(result) < 4:
            result = result[0:2] + '0' + result[2:]
        result = result[2:]
    if by == 11:
        result = multiplication_by_11[int(num[0], 16)][int(num[1], 16)]
        result = str(hex(result))
        if len(result) < 4:
            result = result[0:2] + '0' + result[2:]
        result = result[2:]
    if by == 13:
        result = multiplication_by_13[int(num[0], 16)][int(num[1], 16)]
        result = str(hex(result))
        if len(result) < 4:
            result = result[0:2] + '0' + result[2:]
        result = result[2:]
    if by == 14:
        result = multiplication_by_14[int(num[0], 16)][int(num[1], 16)]
        result = str(hex(result))
        if len(result) < 4:
            result = result[0:2] + '0' + result[2:]
        result = result[2:]
    return result


def xor(str1: str, str2: str) -> str:
    """
    xor two strings
    """
    res = str(hex(int(bin(int(str1, 16) ^ int(str2, 16))[2:], 2))[2:])
    return res if len(res) == 2 else '0' + res


def XOR(lis1: list, lis2: list) -> list:
    """
    xor content of 2 lists
    """
    newList = []
    for i in range(len(lis1)):
        b = str(hex(int(bin(int(lis1[i], 16) ^ int(lis2[i], 16))[2:], 2))[2:])
        if len(b) == 1:
            b = '0' + b
            newList.append(b)
        else:
            newList.append(b)
    return newList


def RotWord(lis: list, rotation_value) -> list:
    """
    take a list and rotate it by rotation value to the right
    """
    lis = lis[-rotation_value:] + lis[:-rotation_value]
    return lis


def subWord(lis: list) -> list:
    """
    used in subWord operation on key scheduling
    """
    for i in range(len(lis)):
        lis[i] = sbox[int(str(lis[i])[0], base=16)][int(str(lis[i])[1], base=16)]
    return lis


def Rcon(num: int) -> list:
    """used on key scheduling"""
    rcon = ['01', '02', '04', '08', '10', '20', '40',
            '80', '1B', '36', '6C', 'D8', 'AB', '4D']
    return [rcon[num - 1], '00', '00', '00']


def keyExp(key: list) -> list:
    """
    the main method for the key expansion ,
    taking the key and expand it to
    14 keys + the main key if 256 bit
    10 keys + the main key if 128 bit
    """
    if len(key) == 8:
        words = len(key)
        r = 14
    else:
        words = len(key)
        r = 10

    keysList = [key]
    if r == 10:
        for rnd in range(0, r):
            tempCol = RotWord(key[-1], -1)
            tempCol = subWord(tempCol)
            tempCol = XOR(tempCol, Rcon(rnd + 1))
            tempCol = XOR(tempCol, key[0])
            newKey = [tempCol]
            for i in range(1, words):
                newKey.append(XOR(newKey[i - 1], key[i]))
            keysList.append(newKey)
            key = newKey
    if r == 14:
        for rnd in range(0, r):
            tempCol = RotWord(key[-1], -1)
            tempCol = subWord(tempCol)
            tempCol = XOR(tempCol, Rcon(rnd + 1))
            tempCol = XOR(tempCol, key[0])
            newKey = [tempCol]
            word = 1
            for i in range(1, words):
                if word != 4:
                    newKey.append(XOR(newKey[i - 1], key[i]))
                else:
                    newKey.append(XOR(subWord(newKey[i - 1]), key[i]))
                    newKey[3] = XOR(newKey[i - 2], key[i - 1])
                word = word + 1
            keysList.append(newKey)
            key = newKey

        for lis in range(len(keysList)):
            keysList[lis] = keysList[lis][0:4]
    return keysList


def addRoundKey(key: list, plain: list) -> list:
    cipher = []
    for i in range(0, 4):
        cipher.append(XOR(key[i], plain[i]))
    return cipher


def subBytes(state: list) -> list:
    """
    take a list and convert it's content to the S-box
    """
    for j in state:
        if isinstance(state[0][0], str):
            for i in range(len(j)):
                hexNum = '0x' + j[i]
                # print(int(hexNum[3], 16))
                j[i] = sbox[int(hexNum[2], base=16)][int(hexNum[3], base=16)]
        else:
            for lis in j:
                for i in range(len(lis)):
                    hexNum = '0x' + lis[i]
                    if len(hexNum) < 4:
                        hexNum = hexNum + '0'
                    # print(int(hexNum[3], 16))
                    lis[i] = sbox[int(hexNum[2], base=16)][int(hexNum[3], base=16)]
    return state


def subBytesInv(state: list) -> list:
    """
    inverse subBytes function
    """
    for j in state:
        if isinstance(state[0][0], str):
            for i in range(len(j)):
                hexNum = '0x' + j[i]
                # print(int(hexNum[3], 16))
                j[i] = sboxInv[int(hexNum[2], base=16)][int(hexNum[3], base=16)]
        else:
            for lis in j:
                for i in range(len(lis)):
                    hexNum = '0x' + lis[i]
                    if len(hexNum) < 4:
                        hexNum = hexNum + '0'
                    # print(int(hexNum[3], 16))
                    lis[i] = sboxInv[int(hexNum[2], base=16)][int(hexNum[3], base=16)]
    return state


def ShiftRows(state: list) -> list:
    if isinstance(state[0][0], str):
        for i in range(1, 4):
            temp = []
            for j in range(4):
                temp.append(state[j][i])
            temp = RotWord(temp, -i)
            for j in range(4):
                state[j][i] = temp[j]
    else:
        for lis in state:
            for i in range(1, 4):
                temp = []
                for j in range(4):
                    temp.append(lis[j][i])
                temp = RotWord(temp, -i)
                for j in range(4):
                    lis[j][i] = temp[j]

    return state


def ShiftRowsInverse(state: list) -> list:
    if isinstance(state[0][0], str):
        for i in range(1, 4):
            temp = []
            for j in range(4):
                temp.append(state[j][i])
            temp = RotWord(temp, i)
            for j in range(4):
                state[j][i] = temp[j]
    else:
        for lis in state:
            for i in range(1, 4):
                temp = []
                for j in range(4):
                    temp.append(lis[j][i])
                temp = RotWord(temp, i)
                for j in range(4):
                    lis[j][i] = temp[j]

    return state


def mixColumns(state: list) -> list:
    newState = []
    opList = [2, 3, 1, 1]
    if isinstance(state[0][0], str):
        for i in range(0, 4):
            newRow = []
            for j in range(0, 4):
                copyCol = state[j]
                tempMult = []
                for k in range(0, 4):
                    tempMult.append(mult(copyCol[k], opList[k]))
                newRow.append(xor(xor(tempMult[0], tempMult[1]), xor(tempMult[2], tempMult[3])))
            newState.append(newRow)
            opList = RotWord(opList, 1)
    else:
        for lis in state:
            for i in range(0, 4):
                newRow = []
                for j in range(0, 4):
                    copyCol = lis[j]
                    tempMult = []
                    for k in range(0, 4):
                        tempMult.append(mult(copyCol[k], opList[k]))
                    newRow.append(xor(xor(tempMult[0], tempMult[1]), xor(tempMult[2], tempMult[3])))
                newState.append(newRow)
                opList = RotWord(opList, 1)
    return reverseMatrix(newState)


def mixColumnsInverse(state: list) -> list:
    newState = []
    opList = [14, 11, 13, 9]
    if isinstance(state[0][0], str):
        for i in range(0, 4):
            newRow = []
            for j in range(0, 4):
                copyCol = state[j]
                tempMult = []
                for k in range(0, 4):
                    tempMult.append(mult(copyCol[k], opList[k]))
                newRow.append(xor(xor(tempMult[0], tempMult[1]), xor(tempMult[2], tempMult[3])))
            newState.append(newRow)
            opList = RotWord(opList, 1)
    else:
        for lis in state:
            for i in range(0, 4):
                newRow = []
                for j in range(0, 4):
                    copyCol = lis[j]
                    tempMult = []
                    for k in range(0, 4):
                        tempMult.append(mult(copyCol[k], opList[k]))
                    newRow.append(xor(xor(tempMult[0], tempMult[1]), xor(tempMult[2], tempMult[3])))
                newState.append(newRow)
                opList = RotWord(opList, 1)
    return reverseMatrix(newState)


def encrypt() -> str:
    plainTextBlocks = getLists(str(input("enter plain text : ")))
    keysList = keyExp(inputKey(input("enter the key in hex format : ")))
    for r in range(len(plainTextBlocks)):
        plainTextBlocks[r] = addRoundKey(keysList[0], plainTextBlocks[r])
        for i in range(1, len(keysList)):
            plainTextBlocks[r] = subBytes(plainTextBlocks[r])
            plainTextBlocks[r] = ShiftRows(plainTextBlocks[r])
            if i != len(keysList) - 1:
                plainTextBlocks[r] = mixColumns(plainTextBlocks[r])
            plainTextBlocks[r] = addRoundKey(keysList[i], plainTextBlocks[r])

    cipher = ''
    for lis in plainTextBlocks:
        for li in lis:
            for i in li:
                cipher = cipher + i
    return cipher


def decrypt() -> str:
    plainTextBlocks = convertToMatrix((input("enter encrypted text : ")))
    keysList = keyExp(inputKey(input("enter the key in hex format : ")))
    for r in range(len(plainTextBlocks)):
        for i in range(len(keysList)-1, 0, -1):
            plainTextBlocks[r] = addRoundKey(plainTextBlocks[r], keysList[i])
            if i != len(keysList) - 1:
                plainTextBlocks[r] = mixColumnsInverse(plainTextBlocks[r])
            plainTextBlocks[r] = ShiftRowsInverse(plainTextBlocks[r])
            plainTextBlocks[r] = subBytesInv(plainTextBlocks[r])
        plainTextBlocks[r] = addRoundKey(plainTextBlocks[r], keysList[0])

    cipher = ''
    for lis in plainTextBlocks:
        for li in lis:
            for i in li:
                cipher = cipher + i
    return bytes.fromhex(cipher).decode('utf-8')




