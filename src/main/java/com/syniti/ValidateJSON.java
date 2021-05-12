package com.syniti;

import java.util.List;

import com.syniti.helper.HelperUtility;

public class ValidateJSON {

	
	public static void main(String[] args) {
		
		HelperUtility helperUtility = new HelperUtility();
		List<String> badRecords = helperUtility.processJSON();
		System.out.println("Total bad records found = " + badRecords.size());
		for(String s: badRecords)
			System.out.println(s);
	}
}
