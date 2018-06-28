import sys
sys.path.append("./assest")
import youtube


def main():
    song = youtube.youtube()
    song_data = song.search("周杰倫")

    for i in range(0, 5):
        print(song_data[0][i] + ",\n" + song_data[1][i] + '\n\n')

     
if __name__ == '__main__':
    main()
