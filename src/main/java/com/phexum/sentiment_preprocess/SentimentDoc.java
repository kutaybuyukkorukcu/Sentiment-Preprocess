package com.phexum.sentiment_preprocess;

import java.util.Scanner;

public class SentimentDoc {

	public StringBuffer sentTxt(String file) {

		Scanner input = new Scanner(file);
		int id = 0;
		String sSent = null;
		StringBuffer print = new StringBuffer();
		print.append("ID" + "\t" + "Sent" + "\n");
		while (input.hasNext()) {
			String line = input.nextLine();
			if (line.trim().isEmpty()) {
				continue;
			}
			if (line.contains("------------")) {
				++id; // #ID
				sSent = line.substring(line.length() - 13, line.length() - 12); // #Review Sentimenti
				print.append(id + " " + sSent + "\n");
				continue;
			}
		}
		input.close();
		return print;
	}
}
