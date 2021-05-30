package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"regexp"
)

//Validating data
func ValidateData(indata map[string]interface{}) interface{} {
	var validID = regexp.MustCompile(`^\d{5}(?:[-\s]\d{4})?$`) // regex for US zipcode

	if indata["address"] == nil || indata["address"] == "" ||
		indata["name"] == "" || indata["name"] == nil ||
		indata["zip"] == "" || indata["zip"] == nil {
		return indata["id"]
	} else if indata["zip"] != "" || indata["zip"] != nil { //validating ZIP code
		match := validID.MatchString(indata["zip"].(string))
		if !match && indata["id"] != nil {
			return indata["id"]
		}
		return ""
	}
	return ""
}

// Unmarshalling JSON
func Unmarshal(rawdata []byte) ([]map[string]interface{}, error) {
	var data1 []map[string]interface{}
	err := json.Unmarshal(rawdata, &data1)
	if err != nil {
		return nil, err
	}
	return data1, nil
}

//Checking Duplicate data
func Duplicate(v map[string]interface{}, data []map[string]interface{}) (interface{}, interface{}) {
	for j := 1; j < len(data); j++ {
		if v["address"] != nil && data[j]["address"] != nil &&
			v["address"] == data[j]["address"] &&
			v["id"] != data[j]["id"] {
			return v["id"], data[j]["id"]
		} else if v["name"] != nil && data[j]["name"] != nil &&
			v["name"] == data[j]["name"] &&
			v["id"] != data[j]["id"] {
			return v["id"], data[j]["id"]
		} else if v["zip"] != nil && data[j]["zip"] != nil &&
			v["zip"] == data[j]["zip"] &&
			v["id"] != data[j]["id"] {
			return v["id"], data[j]["id"]
		}
	}
	return "", ""
}

func main() {
	var err error
	raw, err := ioutil.ReadFile("data.json") // Reading Json File
	data, err := Unmarshal(raw)              // Unmarshalling Data
	for _, v := range data {
		invalid := ValidateData(v) //Calling Validate Func
		if invalid != "" {
			fmt.Print("\n", invalid.(string), "\n")
		}
		a, b := Duplicate(v, data)
		if a != nil && b != nil {
			fmt.Print("\n", a, "  ", b, "\n")
		}
	}
	if err != nil {
		fmt.Print("error is :", err) // Printing error
	}
}
