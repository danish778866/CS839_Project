import pandas as pd

def sample_candidates(candidate_set, table_A, table_B, num_pairs, output_file):
    A = pd.read_csv(table_A)
    B = pd.read_csv(table_B)
    CS = pd.read_csv(candidate_set)
    sample = CS.sample(n=num_pairs, random_state=1)
    A.columns = ['A_id', 'id', 'name', 'year', 'duration', 'genre', 'actors', 'Up_System']
    B.columns = ['B_id', 'id', 'name', 'year', 'duration', 'genre', 'actors', 'Up_System']
    m1 = pd.merge(sample, A, on='A_id')
    m2 = pd.merge(m1, B, on='B_id')
    m2.to_csv(output_file, index=False)

def main():
    table_A = "imdb_table"
    table_B = "tmdb_table"
    candidate_set = "candidate_set"
    sample_candidates(candidate_set, table_A, table_B, 50, "sample1.csv")

if __name__ == "__main__":
    main()
