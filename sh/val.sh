python3 /home/andrewkc/Projects/ml-project-3/video_features/main.py \
    feature_type=r21d \
    device="cuda:0" \
    file_with_video_paths="/home/andrewkc/Codes/ml-project-3/paths_val_subset.txt" \
    on_extraction=save_numpy \
    output_path="/home/andrewkc/Projects/ml-p3/features_val/" \
    show_pred=false
