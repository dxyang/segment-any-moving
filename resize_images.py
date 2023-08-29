import os
import glob

import cv2
from pathlib import Path
from tqdm import tqdm

if __name__ == "__main__":
    image_dir = "/data/vision/fisher/expres2/dxyang/localdata/warp/dm-test/rgb"
    output_dir = "/data/vision/fisher/expres2/dxyang/localdata/warp/dm-test/rgb_resized"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    in_width =  3840
    in_height = 2160
    out_width = 640
    out_height = 360

    img_fps = glob.glob(f"{image_dir}/*.png")
    for img_fp in tqdm(img_fps):
        file_name = Path(img_fp).name
        out_fp = f"{output_dir}/{file_name}"

        img = cv2.imread(img_fp)
        assert img.shape[1] == in_width
        assert img.shape[0] == in_height
        resized_img = cv2.resize(img, (out_width, out_height))
        cv2.imwrite(out_fp, resized_img)