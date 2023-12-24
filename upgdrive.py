import subprocess

def download_clean_files(bucket_path, local_path):
    command = ["aws", "s3", "cp", bucket_path, local_path, "--recursive", "--exclude", "*", "--include", "*clean.jpg"]

    try:
  
        subprocess.run(command, check=True)
        print("Arquivos 'clean' baixados com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar arquivos 'clean': {e}")

if __name__ == "__main__":
     bucket_path = "s3://user/client/"
    local_path = "/home/user/repo/BFF/"

    download_clean_files(bucket_path, local_path)
