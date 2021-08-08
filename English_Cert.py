from collections import OrderedDict
import pandas as pd


def English_Cert():
    global major_course_dict
    Core_List = []
    major_course_list = []
    major_course_dict = {}
    screen_pair = []
    poetry_pair = []
    short_story_pair = []
    playwriting_pair = []
    nonfiction_pair = []
    writing_electives = []
    core_units = 0
    screen_pair_units = 0
    poetry_pair_units = 0
    short_story_pair_units = 0
    playwriting_pair_units = 0
    nonfiction_pair_units = 0
    writing_electives_units = 0
    units_dict = {}
    Missing_Course = {}
    student_courses = pd.read_csv("C:/Users/family/Desktop/Programming/studentlist.csv")
    student_courses.sort_values(by=['ID', 'Course'], inplace=True)
    student_courses = student_courses.reset_index(drop=True)
    degree_courses = pd.read_csv("C:/Users/family/Desktop/Programming/Creative_Writing_Certificate.csv")

    # print(student_courses)
    # print(degree_courses)


    def pairs(area_name, course_list):
        global major_course_dict

        for j in range(len(degree_courses[area_name])):
            if student_courses.loc[i, "Course"] == degree_courses.loc[j, area_name]:
                units = student_courses.loc[i, "Units"]
                course_list.append([student_courses.loc[i, "Course"]])
                major_course_list.append([student_courses.loc[i, "Course"]])
                major_course_dict[area_name] = course_list
                print(major_course_dict)
                print(major_course_list)
                return units


    for i in range(len(student_courses)):

        if core_units < 6:
            units = pairs("Core", Core_List)
            if units is None:
                units = 0
            core_units = core_units + units

        if screen_pair_units < 6:
            units = pairs("Screen_Pair", screen_pair)
            if units is None:
                units = 0
            screen_pair_units = screen_pair_units + units

        if poetry_pair_units < 6:
            units = pairs("Poetry_Pair", poetry_pair)
            if units is None:
                units = 0
            poetry_pair_units = poetry_pair_units + units

        if short_story_pair_units < 6:
            units = pairs("Short_Story_Pair", short_story_pair)
            if units is None:
                units = 0
            short_story_pair_units = short_story_pair_units + units

        if playwriting_pair_units < 6:
            units = pairs("Playwriting_Pair", playwriting_pair)
            if units is None:
                units = 0
            playwriting_pair_units = playwriting_pair_units + units

        if nonfiction_pair_units < 6:
            units = pairs("NonFiction_Pair", nonfiction_pair)
            if units is None:
                units = 0
            nonfiction_pair_units = nonfiction_pair_units + units

        if writing_electives_units < 6:
            units = pairs("Writing_Electives", writing_electives)
            if units is None:
                units = 0
            writing_electives_units = writing_electives_units + units

        if i <= len(student_courses) - 2:

            if student_courses.loc[i, 'ID'] != student_courses.loc[i + 1, 'ID']:

                if 'Core' in major_course_dict:
                    if len(major_course_dict['Core']) <= 2:
                        core_missing_course = 2 - len(major_course_dict['Core'])
                        Missing_Course['Core'] = core_missing_course

                if 'Screen_Pair' in major_course_dict:
                    if len(major_course_dict['Screen_Pair']) <= 2:
                        screen_pair_missing_course = 2 - len(major_course_dict['Screen_Pair'])
                        Missing_Course['Screen_Pair'] = screen_pair_missing_course

                    if len(major_course_dict['Poetry_Pair']) <= 2:
                        poetry_pair_missing_course = 2 - len(major_course_dict['Poetry_Pair'])
                        Missing_Course['Poetry_Pair'] = poetry_pair_missing_course

                if len(major_course_dict['Short_Story_Pair']) < 2:
                    Short_Story_Pair_missing_course = 1 - len(major_course_dict['Short_Story_Pair'])
                    Missing_Course['Short_Story_Pair'] = Short_Story_Pair_missing_course

                if 'Playwriting_Pair' in major_course_dict:
                    if len(major_course_dict['Playwriting_Pair']) <= 2:
                        Playwriting_Pair_missing_course = 2 - len(major_course_dict['Playwriting_Pair'])
                        Missing_Course['Playwriting_Pair'] = Playwriting_Pair_missing_course

                if 'NonFiction_Pair' in major_course_dict:
                    if len(major_course_dict['NonFiction_Pair']) <= 2:
                        NonFiction_Pair_missing_course = 2 - len(major_course_dict['NonFiction_Pair'])
                        Missing_Course['NonFiction_Pair'] = NonFiction_Pair_missing_course

                if 'Writing_Electives' in major_course_dict:
                    if len(major_course_dict['Writing_Electives']) <= 2:
                        Writing_Electives_missing_course = 2 - len(major_course_dict['Writing_Electives'])
                        Missing_Course['Writing_Electives'] = Writing_Electives_missing_course

                od = OrderedDict(sorted(major_course_dict.items()))
                if 'Core' in major_course_dict:
                    if len(major_course_dict['Core']) == 2:
                        print("Core courses complete")
                    if len(major_course_dict['Core']) < 2:
                        print(f"Student needs to complete {Missing_Course['Core']}")

                DictA = {'Screen_Pair': '2', 'Poetry_Pair': '1', 'Short_Story_Pair': '1', 'Playwriting_Pair': '1', 'NonFiction_Pair':'1'}

                for key in DictA:
                    if key in Missing_Course:
                        if Missing_Course[key] == 0:
                            print(f"Student completed {key} pair")
                            Pairs = True
                            break
                if not Pairs:
                    if len(major_course_dict['Writing_Electives']) == 2:
                        print("Writing Electives courses complete")
                    if len(major_course_dict['Core']) < 2:
                        print(f"Student needs to complete {Missing_Course['Writing_Electives']}")

                Core_List = []
                major_course_list = []
                major_course_dict = {}
                screen_pair = []
                poetry_pair = []
                short_story_pair = []
                playwriting_pair = []
                nonfiction_pair = []
                writing_electives = []
                core_units = 0
                screen_pair_units = 0
                poetry_pair_units = 0
                short_story_pair_units = 0
                playwriting_pair_units = 0
                nonfiction_pair_units = 0
                writing_electives_units = 0
                units_dict = {}
                Missing_Course = {}



    #print(major_course_dict['Writing_Electives'])
