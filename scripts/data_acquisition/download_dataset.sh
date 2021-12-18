#/bin/bash
rm "${BTC_DATAFRAME_PATH}*"
wget https://www.kaggle.com/cstein06/tutorial-to-the-g-research-crypto-competition/data?select=supplemental_train.csv -P "${BTC_DATAFRAME_PATH}"
