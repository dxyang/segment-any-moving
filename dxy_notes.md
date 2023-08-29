# Calculate flow with flownet
```bash
python -m release.custom.compute_flow \
--frames-dir ~/localdata/warp/dm-test/rgb \
--config ./release/config.yaml \
--output-dir ~/localdata/warp/dm-test/flow

python -m flow.compute_flow_sequences \
--input-dir ~/localdata/warp/dm-test/rgb \
--recursive \
--convert-to-angle-magnitude-png on \
--extensions .jpg .jpeg .png .ppm .bmp .pgm \
--gpus 0 \
--num-workers 8 \
--output-dir ~/localdata/warp/dm-test/flow \
--flow-type flownet2 \
--flownet2-dir /home/dxyang/code/segment-any-moving/flownet2 \
--flownet2-model kitti \
--quiet

cd flownet2
pyenv activate segment_moving_38
source set-env.sh
python scripts/run-flownet-many.py \
    models/FlowNet2-KITTI/FlowNet2-KITTI_weights.caffemodel.h5 \
    models/FlowNet2-KITTI/FlowNet2-KITTI_deploy.prototxt.template \
    list.txt \
    --gpu 0
python scripts/run-flownet.py \
    models/FlowNet2-KITTI/FlowNet2-KITTI_weights.caffemodel.h5 \
    models/FlowNet2-KITTI/FlowNet2-KITTI_deploy.prototxt.template \
    /home/dxyang/localdata/warp/dm-test/rgb/frame_002137.png \
    /home/dxyang/localdata/warp/dm-test/rgb/frame_002138.png \
    /home/dxyang/localdata/warp/dm-test/flow/frame_002137.flo \
    --gpu 0
```

# Run detections

## motion + appearance
```bash
python -m release.custom.infer \
--frames-dir ~/localdata/warp/dm-test/rgb_resized \
--flow-dir ~/localdata/warp/dm-test/flow \
--model joint \
--config ./release/config.yaml \
--output-dir ~/localdata/warp/dm-test/detections_joint_005 \
--visualize \
--vis-threshold 0.05
```

## motion
```bash
python -m release.custom.infer \
--frames-dir ~/localdata/warp/dm-test/rgb_resized \
--flow-dir ~/localdata/warp/dm-test/flow \
--config ./release/config.yaml \
--model motion \
--output-dir ~/localdata/warp/dm-test/detections_motion_005 \
--visualize \
--vis-threshold 0.05
```

## appearance
```bash
python -m release.custom.infer \
--frames-dir ~/localdata/warp/dm-test/rgb_resized \
--flow-dir ~/localdata/warp/dm-test/flow \
--model appearance \
--config ./release/config.yaml \
--output-dir ~/localdata/warp/dm-test/detections_rgb_005 \
--visualize \
--vis-threshold 0.05
```

# Run detections low threshold

## motion + appearance
```bash
python -m release.custom.infer \
--frames-dir ~/localdata/warp/dm-test/rgb \
--flow-dir ~/localdata/warp/dm-test/flow \
--model joint \
--config ./release/config.yaml \
--output-dir ~/localdata/warp/dm-test/detections_joint \
--visualize \
--vis-threshold 0.1
```

## motion
```bash
python -m release.custom.infer \
--frames-dir ~/localdata/warp/dm-test/rgb \
--flow-dir ~/localdata/warp/dm-test/flow \
--config ./release/config.yaml \
--model motion \
--output-dir ~/localdata/warp/dm-test/detections_motion \
--visualize \
--vis-threshold 0.1
```

## appearance
```bash
python -m release.custom.infer \
--frames-dir ~/localdata/warp/dm-test/rgb \
--flow-dir ~/localdata/warp/dm-test/flow \
--model appearance \
--config ./release/config.yaml \
--output-dir ~/localdata/warp/dm-test/detections_rgb \
--visualize \
--vis-threshold 0.1
```


# Run tracks

## motion + appearance
```bash
python -m release.custom.track \
--frames-dir ~/localdata/warp/dm-test/rgb \
--detections-dir ~/localdata/warp/dm-test/detections_joint \
--model joint \
--config ./release/config.yaml \
--output-dir ~/localdata/warp/dm-test/tracks_joint

```

## motion
```bash
python -m release.custom.track \
--frames-dir ~/localdata/warp/dm-test/rgb \
--detections-dir ~/localdata/warp/dm-test/detections_motion \
--config ./release/config.yaml \
--model motion \
--output-dir ~/localdata/warp/dm-test/tracks_motion

```

## appearance
```bash
python -m release.custom.track \
--frames-dir ~/localdata/warp/dm-test/rgb \
--detections-dir ~/localdata/warp/dm-test/detections_rgb \
--config ./release/config.yaml \
--model appearance \
--output-dir ~/localdata/warp/dm-test/tracks_rgb
```