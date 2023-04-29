class DataStorage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # kernel constants
            cls._instance.TOP_KERNEL = 33
            cls._instance.LOW_KERNEL = 3

            # binarny
            cls._instance.binary_block=5
            cls._instance.binary_C=-10
            cls._instance.HIGH_C=-5
            cls._instance.LOW_C=-95

            # canny
            cls._instance.canny_treshhold1=50
            cls._instance.canny_treshhold2=150
            cls._instance.HIGH_THRESHHOLD=255
            cls._instance.LOW_THRESHHOLD=0

            #dilate
            cls._instance.dilate_kernel=5

            #erode
            cls._instance.erode_kernel=5

            #gauss
            cls._instance.gauss_kernel=5
            cls._instance.gauss_sigma=1

            #laplace
            cls._instance.laplace_kernel=5

            #median
            cls._instance.median_kernel=5

            #morph
            cls._instance.morph_kernel=5
            
            #compress
            cls._instance.compression_rate=50
        return cls._instance