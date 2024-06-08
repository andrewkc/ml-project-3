python video_features/main.py \
    feature_type=r21d \
    device="cuda:0" \
    file_with_video_paths="/home/andrewkc/Projects/ml-p3/paths_train_data.txt" \
    on_extraction=save_numpy \
    output_path="/home/andrewkc/Projects/ml-p3/features/" \
    show_pred=false