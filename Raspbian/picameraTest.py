import time
import picamera

# 사진
camera = picamera.PiCamera()
try:
    camera.start_preview()
    time.sleep(10)
    camera.stop_preview()
finally:
    camera.close()

# 동영상
# with picamera.PiCamera() as cam:
#     cam.resolution = (640, 480)
#     cam.start_preview()
#     cam.start_recording('foo.h264')
#     cam.wait_recording(5) # 초단위
#     cam.stop_recording()
#     cam.stop_preview()

# 영상 캡처
# with picamera.PiCamera() as cam:
#     cam.resolution = (1280, 720)
#     cam.start_preview()
#     cam.exposure_compensation = 2
#     cam.exposure_mode = 'spotlight'
#     cam.meter_mode = 'matrix'
#     cam.image_effect = 'gpen'
#     # Give the camera some time to adjust to conditions
#     time.sleep(2)
#     cam.exif_tags['IFD0.Artist'] = 'Lim'
#     cam.exif_tags['IFD0.Copyright'] = 'CR Lim'
#     cam.capture('foo.jpg')
#     cam.stop_preview()