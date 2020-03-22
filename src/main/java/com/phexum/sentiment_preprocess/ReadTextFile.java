package com.phexum.sentiment_preprocess;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class ReadTextFile {

	public String readTextFile(String fileName) throws FileNotFoundException, IOException {
		String returnValue = "";
		FileReader file;
		String line = "";

		file = new FileReader(fileName);
		BufferedReader reader = new BufferedReader(file);
		while ((line = reader.readLine()) != null) {
			returnValue += line + "\n";
		}
		reader.close();
		return returnValue;

	}
}
