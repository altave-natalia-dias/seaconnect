import subprocess

def download_clean_files(bucket_path, local_path):
    # Comando AWS CLI para baixar os arquivos "clean"
    command = ["aws", "s3", "cp", bucket_path, local_path, "--recursive", "--exclude", "*", "--include", "*clean.jpg"]

    try:
        # Executar o comando usando subprocess
        subprocess.run(command, check=True)
        print("Arquivos 'clean' baixados com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar arquivos 'clean': {e}")

if __name__ == "__main__":
    # Substitua os valores abaixo com o caminho do bucket S3 e o caminho local desejado
    bucket_path = "s3://harpia-alerts/valaris_ds8/"
    local_path = "/home/altave/repo/BFF/"

    download_clean_files(bucket_path, local_path)
