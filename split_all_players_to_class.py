import pandas as pd

runner_data = pd.read_csv("all_players.csv",header=0)

#print(runner_data['handle'])


for i in range(1,5):
    file_name = ''
    class_df = pd.DataFrame(columns=['handle'])
    for runner in runner_data['handle']:
        handle = ''
        handle = str(runner)
        if int(handle[0]) == i:
            class_df.loc[len(class_df.index)] = [handle]
    file_name = str(i) + "A.csv"
    class_df.to_csv(file_name, index=False)

