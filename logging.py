import logging
import subprocess

def download_clean_files(bucket_path, local_path):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    command = [
        "aws",
        "s3",
        "cp",
        bucket_path,
        local_path,
        "--recursive",
        "--exclude", "*",
        "--include", "*clean.jpg"
    ]

    try:
        subprocess.run(command, check=True)
        logger.info("Arquivos 'clean' baixados com sucesso.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Erro ao baixar arquivos 'clean': {e}")

if __name__ == "__main__":
    bucket_path = "s3://user/client/"
    local_path = "/home/user/repo/BFF/"

    download_clean_files(bucket_path, local_path)
