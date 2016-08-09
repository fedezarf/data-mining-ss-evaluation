#!/bin/bash
declare -a stemmers=("default" "english" "stop" )
declare -a scorers=( "CountScorer" "tfidf" "BM25Scorer" )

for s in "${stemmers[@]}"
do
	for k in "${scorers[@]}"
	do		
		ipython evaluatePerformance.py output_cran_"$s"_"$k".tsv cran_Ground_Truth.tsv			
		((i++))
	done
done

echo "Performance of Stemmer-Scorer combinations on Cranfield Data done"