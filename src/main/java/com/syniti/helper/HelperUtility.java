package com.syniti.helper;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.regex.Pattern;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.syniti.models.Person;

public class HelperUtility {

	

	public List<Person> readJson() {
		 List<Person> persons =null;
		try {
		    Gson gson = new Gson();

		    Reader reader = Files.newBufferedReader(Paths.get("data.json"));

		    persons = new Gson().fromJson(reader, new TypeToken<List<Person>>() {}.getType());

		    //persons.forEach(System.out::println);

		    reader.close();

		} catch (Exception ex) {
		    ex.printStackTrace();
		}
		return persons;
	}

	public List<String> processJSON() {
		List<Person> personList = readJson();
		HashSet<String> badRecords = new HashSet<String>();
		
	        HashMap<Person,Person> uniquePerson = new HashMap<>();
	        for(Person person: personList){
	        	/*
	        	if(person.getZip()!=null && !person.getZip().matches("^[0-9]{5}(?:-[0-9]{4})?$"))
		        	   System.out.println(person);
		        	*/   
	           if(person.getAddress() == null || person.getName() == null || person.getZip() == null ||
	        		   person.getAddress().equals("") || person.getName().equals("")  || person.getZip().equals("") 
	        		   ||  !person.getZip().matches("^[0-9]{5}(?:-[0-9]{4})?$")) {
	        	   
	        	   
	        	   badRecords.add(person.getId());
	        	  
	           }
	           else if(uniquePerson.containsKey(person) ) {
	        	   badRecords.add(person.getId());
	        	   badRecords.add(uniquePerson.get(person).getId());
	           }
	           else {
	        	   uniquePerson.put(person,person);
	           }
	        }
	        
	        return new ArrayList<>(badRecords) ;
	        
	}

}
