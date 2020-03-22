package com.phexum.sentiment_preprocess;

import java.io.FileNotFoundException;
import java.io.IOException;

public class Application {

	public static void main(String[] args) throws FileNotFoundException, IOException {
		ReadTextFile out = new ReadTextFile();
		WriteTextFile in = new WriteTextFile();
		ReviewDoc rDoc = new ReviewDoc();
		in.setPath("./files/reviewOutput.txt");
		in.writeTextFile(rDoc.reviewTxt(out.readTextFile("./files/input.txt")));
		SentimentDoc sDoc = new SentimentDoc();
		in.setPath("./files/sentimentOutput.txt");
		in.writeTextFile(sDoc.sentTxt(out.readTextFile("./files/input.txt")));
	}
}
