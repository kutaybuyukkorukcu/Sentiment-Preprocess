package com.phexum.sentiment_preprocess;

import java.util.Scanner;

public class ReviewDoc {

	public StringBuffer reviewTxt(String file) {
		
		Scanner input = new Scanner(file);
		int id = 0;
		int docId = 0;
		String rSent = null;
		String txt = null;
		StringBuffer print = new StringBuffer();
		print.append("ID" + "\t" + "docID" + "\t" + "Sent" + "\t" + "Text" + "\n");
		while (input.hasNext()) {
			String line = input.nextLine();
			if (line.trim().isEmpty()) {
				continue;
			}
			if (line.contains("------------")) {
				++id;
				docId = 0;
				continue;
			}
			++docId;
			char m = (line.charAt(line.length() - 1));
			if (m == 'n' || m == 'p' || m == 'o') {
				line += ("," + docId);
				docId = Integer.parseInt(line.substring(line.length() - 1)); // #docID
				int ilkI = line.indexOf(",");
				rSent = line.substring(ilkI - 1, ilkI); // #Text sentimenti
				txt = line.substring(0, line.lastIndexOf(",") - 1);
				print.append((id + "\t" + docId + "\t" + "\t" + rSent + "\t" + "\t" + txt + "\n"));
				continue;
			}

		}
		input.close();
		return print;
	}
}
