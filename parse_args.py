import argparse
import datetime



def main_parse_args():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('--fp16', action='store_true')
    parser.add_argument('--cpu', action='store_true', help='To use CPU')
    parser.add_argument('--tune', action='store_true', help='To perform optuna model tuning for LR and optimiser')

    parser.add_argument(
        '--output_dir', 
        type=str, 
        default=None,
        help='Output dir for this experiment'
    )

    parser.add_argument(
        '--dataset', 
        type=str, 
        default='fashionmnist',
        help='Can be "fashionmnist" or "cifar10"'
    )

    parser.add_argument(
        '--resnet_version',
        type=str,
        default='101',
        help='ResNet version to use. Supports 50, 101 and 152.'
    )
    
    # Replace the `x` layer in the i_th conv block with deformable convolution
    parser.add_argument('--with_deformable_conv', nargs=4, type=int, default=[0,0,0,0], help='No. of conv layers to replace with deformable conv in ResNet block 2 to 5')

    # Unfreezing the last `x` 3*3 conv layer in i_th conv block
    parser.add_argument('--unfreeze_conv', nargs=4, type=int, default=[0,0,0,0], help='No. of conv layers to unfreeze in ResNet block 2 to 5')

    parser.add_argument('--unfreeze_offset', action='store_true', help='Unfreeze all offsets')
    parser.add_argument('--unfreeze_fc', action='store_true', help='Unfreeze output layer')

    parser.add_argument('--model_weights', type=str, default=None, help="File path to model's weight")

    # With early stopping
    parser.add_argument('--early_stopping', action='store_true', help='Use early_stopping')

    parser.add_argument(
        "--patience",
        type=int,
        default=5,
        help="patience for early stopping",
    )
    parser.add_argument(
        "--mode", type=str, default='min', help="optimise towards minimising or maximising loss function. Supports 'min' or 'max'"
    )
    parser.add_argument(
        "--min_delta",
        type=float,
        default=0.0005,
        help="minimum difference in performance for early stopping",
    )

    parser.add_argument('--restore_best_weights', action='store_true', help="Use best weights to test evaluation")

    # Learning rate
    parser.add_argument(
        "--learning_rate",
        type=float,
        default=0.0005,
        help="Learning Rate",
    )
    # Train batch size
    parser.add_argument(
        "--train_batch_size",
        type=int,
        default=32,
        help="Batch size for the training dataloader."
    )

    # Batch size for both test and val dataloader
    parser.add_argument(
        "--eval_batch_size",
        type=int,
        default=32,
        help="Batch size for the val and test dataloader.",
    )

    parser.add_argument("--num_epochs", type=int, default=10, help="Total number of training epochs to perform.")

    parser.add_argument('--debug', action='store_true', help='Run on subset of data')

    args = parser.parse_args()

    return args


def offset_parse_args():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('--video', action='store_true')
    parser.add_argument(
        '--fps',
        type=int,
        help='FPS for the video'
    )
    parser.add_argument(
        '--duration',
        type=int,
        help='Duration for the video'
    )

    parser.add_argument(
        '--output_dir', 
        type=str,
        help='Output Dir'
    )

    parser.add_argument(
        '--image_file', 
        type=str,
        help='Image file to generate'
    )

    parser.add_argument(
        '--model_weights', 
        type=str,
        help='Model Weights '
    )


    parser.add_argument(
        '--resnet_version',
        type=str,
        default='101',
        help='Which resnet version to use'
    )
    
    # Replace the `x` layer in each resnet block with deformable convolution
    parser.add_argument('--with_deformable_conv', nargs=4, type=int, default=[0,0,0,0])

    # Unfreezing the last `x` 3*3 conv layer in corresponding resnet block
    parser.add_argument('--unfreeze_conv', nargs=4, type=int, default=[0,0,0,0])

    parser.add_argument('--unfreeze_offset', action='store_true')
    parser.add_argument('--unfreeze_fc', action='store_true')

    parser.add_argument('--num_classes', type=int, default=10)


    args = parser.parse_args()

    return args