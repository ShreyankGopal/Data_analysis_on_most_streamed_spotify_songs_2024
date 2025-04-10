# Data Visualization (DAS 732) - Assignment 3
## View the report.pdf to get a complete analysis report
## Datasets Used

1. Most Streamed Spotify Songs 2024 'https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024/data'
3. Spotify Tracks Genre Dataset 'https://www.kaggle.com/datasets/thedevastator/spotify-tracks-genre-dataset/data'

## Preprocessing

Although the cleaned and merged datasets have been added to a separate folder, the preprocessing codes have also been added.

For the assignment 1 dataset (most_streamed_spotify_songs_2024.csv), use the Python scripts in ```src/Preprocessing/A1 Preprocessing``` to obtain the cleaned and processed dataset.

For the assignment 2 dataset (train.csv), execute the Python notebooks in the order:

1. run ```src/Preprocessing/FixDataset.ipynb```
2. run ```src/Preprocessing/Merging.ipynb```

## Workflow-1

### Iteration 1

The code for plotting the visualisation can be found in:

```src/Workflow-1/Iteration-1/Loop1.ipynb```

### Iteration 2

-To run the visualisation plotting codes use the command 
```bash 
python3 src/Workflow-1/Iteration-2/iteration2.py

```

### Iteration 3

The supervised models that were used for classification can be found in:

```src/Workflow-1/Iteration-1/Iteration3.ipynb```

### Iteration 4

-To run the PCP plots first ensure that you have the VS code's live server extension. The navigate to teh directory from the DV_assignment_3 directory using the following command
```bash
cd src/Workflow-1/Iteration-4
```
Right click on the html files and click on open with live server. The PCP will be plotted on local host.

## Workflow-2
The code for plotting the visualizations can be found in the ```src/Workflow-2``` folder

Inorder to run the source code, simply run ```python3 src/Workflow-2/Iteration-x/Loop_1.ipynb``` to see the visualizations get created.

The ```plt.show()``` line of code is uncommented inorder to be able to quickly see the visualizations.
