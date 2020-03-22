package com.phexum.sentiment_preprocess;

import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;

public class WriteTextFile {
	
	private String path;
	
	public String getPath() {
		return path;
	}

	public void setPath(String path) {
		this.path = path;
	}

	public void writeTextFile(StringBuffer print) throws FileNotFoundException, IOException {
		BufferedWriter writer = new BufferedWriter (new OutputStreamWriter((new FileOutputStream(path)), StandardCharsets.UTF_8));
		writer.write(print.toString());
		writer.close();
	}
	
}
