import os

import zipfile

import pandas as pd

class ZipDataIngestor(DataIngestor):
  def ingest(self, file_path: str) -> pd.DataFrame:
    ""Extract a .zip file and returns the content as a panda DataFrame.""
    if not file_path.endswith(".zip"):
      raise ValueError("The provided file is not in zip format.")

    with zipfile.ZipFile(file_path,"r") as zip_red:
      zip_ref.extractall("extracted_data")
