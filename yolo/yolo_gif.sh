#mkdir -p frames
#mkdir -p resized
#mkdir -p preds
#python get_frames.py
for file in ./resized/*
do
        ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights ${file: 2}
        cp predictions.jpg preds/pred_${file: 14}
done
python make_gif.py
rm preds/*
rm resized/*
rm frames/*