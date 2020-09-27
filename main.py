import os
import modules
import sys


def main():
    #input Sentinel-5p file
    source_file=input('input file path: ')
    while os.path.exists(source_file) is False:
        print("file doesn't exist, input again!")
        source_file=input('input file path: ')
    # Choose product NO2 or SO2
    if 'NO2' in source_file:
        classify = 1
    elif 'SO2' in source_file:
        classify = 2
    else:
        print('Cannot find NO2 or SO2 product, program exit!!!')
        sys.exit(0)._exit()

    if classify == 1 :     ##### NO2 processing ########
        print ('Please choose the product that you want to visualize')
        print('Tropospheric vertical column of nitrogen dioxide: Press 1 + Enter')
        print('Tropospheric nitrogen dioxide precision: Press 2 + Enter')
        class_no2 = int(input('choose product: '))       
        while class_no2 != 1 and class_no2 != 2:
            print("Please choose just 1 or 2")
            class_no2 = int(input('choose product: '))
        if class_no2 == 1 :
            source_data=modules.no2_col(source_file)
            check = 'NO2_tropospheric_column'
            modules.plot_for_no2(source_data['data'], source_data['lons'], source_data['lats'], check)
        else:
            source_data=modules.no2_pre(source_file)
            check = 'NO2_tropospheric_column_precision'
            modules.plot_for_no2(source_data['data'], source_data['lons'], source_data['lats'], check)
    else:
        print ('Please choose the product that you want to visualize')
        print('Total vertical column of sulfur dioxide for the polluted scenario derived from the total slant column: Press 1 + Enter')
        print('Precision of the total vertical column of sulfur dioxide for the polluted scenario derived from the total slant column: Press 2 + Enter')
        class_so2 = int(input('choose product: '))       
        while class_so2 != 1 and class_so2 != 2:
            print("Please choose just 1 or 2")
            class_so2 = int(input('choose product: '))
        if class_so2 == 1 :
            source_data=modules.so2_col(source_file)
            check = 'SO2_total_vertical_column'
            modules.plot_for_so2(source_data['data'], source_data['lons'], source_data['lats'], check)
        else:
            source_data=modules.so2_pre(source_file)
            check = 'SO2_total_vertical_column_precision'
            modules.plot_for_so2(source_data['data'], source_data['lons'], source_data['lats'], check)


if __name__ == '__main__':
    main()
    print('.::Done::.')
        