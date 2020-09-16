import splitfolders 

if __name__ == "__main__":
    
    splitfolders.ratio('data/audio/chunks', 'data/audio/split_chunks', ratio=(.8, .1, .1))