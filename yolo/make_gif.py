"""create gif out of images"""
import imageio
import os

IN_DIRECTORY = "preds"
OUTPUT = "output"
FPS = 30




def create_gif(input_directory, output, fps=30):
    images = []
    dir_length = len([name for name in os.listdir(f"./{input_directory}") if os.path.isfile(os.path.join(f"./{input_directory}", name))])
    for i in range(0, dir_length):
        filename = f"{input_directory}/pred_{i}.jpg"
        images.append(imageio.imread(filename))

    imageio.mimsave(f"{output}.gif", images, fps=fps)


if __name__ == "__main__":
    create_gif(IN_DIRECTORY, OUTPUT, 30)
