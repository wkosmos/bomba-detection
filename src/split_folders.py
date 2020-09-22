import splitfolders 

if __name__ == "__main__":
    
    splitfolders.ratio('data/audio/400_chunks', 'data/audio/400_chunks_split', ratio=(.8, .1, .1))