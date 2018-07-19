import csv
import googlemaps
gmaps = googlemaps.Client(key='-----')

def process_line(line):
    # makes modifications to an address, if applicable
    if line[8] == "":
        #to account for entries w/o addresses
        return("")
    if len(line[8]) < 5:
        #to account for entries with 4-digit zip codes
        line[8] = '0' + line[8]
    if len(line[8]) == 9:
        #to account for extended 4-digit zip codes
        line[8] = '0' + line[8]

def geocode_line(line):
    # performs conversion from written address to coordinates
    if "c/o" in line[2]:
        return(gmaps.geocode(line[3] + " " + line[4] + " " + line[5] + " " + line[6] + " " + line[7] + " " + line[8]))
    else:
        return (gmaps.geocode(line[2] + " " + line[3] + " " + line[4] + " " + line[5] + " " + line[6] + " " + line[7] + " " + line[8]))


ad_file = open('sample.csv', 'r')
reader = csv.reader(ad_file, delimiter=',')

no_c_file = open('sample_no_coordinates.csv', 'w', newline='')
writer = csv.writer(no_c_file)

bad_c_file = open('sample_bad_coordinates.csv', 'w', newline='')
writer1 = csv.writer(bad_c_file)

good_c_file = open('sample_good_coordinates.csv', 'w', newline='')
writer2 = csv.writer(good_c_file)

for line in reader:
    processing = process_line(line)
    geocoding = geocode_line(line)
    if processing == "":
        # if process_line is empty, then write line[0] into the null address file
        no_result = [line[0], "ERROR", "######", str(line[1] + " " + line[2] + " " + line[3] + " " + line[5] + " " +
                                                     line[6] + " " + line[7] + " " + line[8])]
        writer.writerow(no_result)
    elif geocoding == []:
        # if geocoding returns with an error, write line[0] to the bad address file
        b_result = [line[0], "ERROR", "######", str(line[1] + " " + line[2] + " " + line[3] + " " + line[5] + " " +
                                                    line[6] + " " + line[7] + " " + line[8])]
        writer1.writerow(b_result)
    else:
        # otherwise, write successfully geocoded addresses to the good file
        g_result = [line[0], geocoding[0]['geometry']['location']['lat'], geocoding[0]['geometry']['location']['lng']]
        writer2.writerow(g_result)

ad_file.close()
no_c_file.close()
bad_c_file.close()
good_c_file.close()
