export default {
  barLabelInfo: [
    {
      label: 'animal',
      modelsInfo: [
        {
          model: 'mobilenet_v2',
          labelList: ['102', '376', '275', '167', '240', '282'],
          labelAcc: [100.0, 100.0, 100.0, 28.0, 26.0, 18.0]
        },
        {
          model: 'alexnet',
          labelList: ['90', '376', '275', '62', '167', '124'],
          labelAcc: [100.0, 98.0, 96.0, 14.0, 14.0, 14.0]
        },
        {
          model: 'resnet18',
          labelList: ['364', '13', '275', '68', '240', '282'],
          labelAcc: [100.0, 100.0, 100.0, 22.0, 22.0, 12.0]
        },
        {
          model: 'resnet34',
          labelList: ['275', '333', '19', '282', '167', '68'],
          labelAcc: [100.0, 100.0, 100.0, 28.0, 22.0, 18.0]
        },
        {
          model: 'resnet50',
          labelList: ['102', '376', '275', '167', '282', '240'],
          labelAcc: [100.0, 100.0, 100.0, 30.0, 22.0, 20.0]
        },
        {
          model: 'resnet101',
          labelList: ['364', '9', '146', '167', '240', '282'],
          labelAcc: [100.0, 100.0, 100.0, 32.0, 30.0, 18.0]
        },
        {
          model: 'resnet152',
          labelList: ['125', '102', '275', '167', '240', '282'],
          labelAcc: [100.0, 100.0, 100.0, 36.0, 36.0, 24.0]
        },
        {
          model: 'densenet121',
          labelList: ['364', '9', '13', '60', '240', '282'],
          labelAcc: [100.0, 100.0, 100.0, 38.0, 20.0, 18.0]
        },
        {
          model: 'densenet161',
          labelList: ['275', '102', '255', '60', '68', '282'],
          labelAcc: [100.0, 100.0, 100.0, 36.0, 34.0, 20.0]
        },
        {
          model: 'densenet169',
          labelList: ['275', '9', '376', '60', '68', '282'],
          labelAcc: [100.0, 100.0, 100.0, 32.0, 26.0, 18.0]
        },
        {
          model: 'densenet201',
          labelList: ['129', '13', '333', '167', '240', '282'],
          labelAcc: [100.0, 100.0, 100.0, 36.0, 30.0, 26.0]
        },
        {
          model: 'squeezenet1_1',
          labelList: ['340', '376', '275', '240', '62', '167'],
          labelAcc: [96.0, 96.0, 96.0, 20.0, 20.0, 18.0]
        },
        {
          model: 'shufflenet_v2_x0_5',
          labelList: ['275', '139', '351', '60', '68', '282'],
          labelAcc: [100.0, 98.0, 98.0, 16.0, 16.0, 16.0]
        }
      ]
    },
    {
      label: 'artifact',
      modelsInfo: [
        {
          model: 'mobilenet_v2',
          labelList: ['565', '645', '916', '836', '782', '885'],
          labelAcc: [100.0, 100.0, 100.0, 14.0, 10.0, 10.0]
        },
        {
          model: 'alexnet',
          labelList: ['472', '685', '645', '885', '836', '813'],
          labelAcc: [96.0, 94.0, 94.0, 6.0, 6.0, 6.0]
        },
        {
          model: 'resnet18',
          labelList: ['607', '565', '781', '620', '885', '836'],
          labelAcc: [98.0, 98.0, 96.0, 12.0, 12.0, 8.0]
        },
        {
          model: 'resnet34',
          labelList: ['645', '565', '874', '818', '620', '885'],
          labelAcc: [98.0, 98.0, 98.0, 14.0, 14.0, 10.0]
        },
        {
          model: 'resnet50',
          labelList: ['576', '500', '916', '620', '885', '638'],
          labelAcc: [100.0, 100.0, 100.0, 22.0, 18.0, 18.0]
        },
        {
          model: 'resnet101',
          labelList: ['874', '645', '554', '620', '885', '782'],
          labelAcc: [100.0, 100.0, 100.0, 20.0, 18.0, 16.0]
        },
        {
          model: 'resnet152',
          labelList: ['554', '535', '816', '818', '782', '885'],
          labelAcc: [100.0, 100.0, 100.0, 24.0, 22.0, 22.0]
        },
        {
          model: 'densenet121',
          labelList: ['685', '576', '645', '836', '885', '782'],
          labelAcc: [100.0, 98.0, 98.0, 14.0, 14.0, 12.0]
        },
        {
          model: 'densenet161',
          labelList: ['565', '535', '915', '818', '782', '638'],
          labelAcc: [100.0, 100.0, 100.0, 26.0, 22.0, 20.0]
        },
        {
          model: 'densenet169',
          labelList: ['554', '466', '916', '818', '620', '782'],
          labelAcc: [100.0, 100.0, 100.0, 20.0, 18.0, 14.0]
        },
        {
          model: 'densenet201',
          labelList: ['565', '554', '800', '638', '818', '782'],
          labelAcc: [100.0, 100.0, 100.0, 22.0, 22.0, 18.0]
        },
        {
          model: 'squeezenet1_1',
          labelList: ['565', '607', '625', '885', '838', '784'],
          labelAcc: [96.0, 94.0, 92.0, 10.0, 10.0, 10.0]
        },
        {
          model: 'shufflenet_v2_x0_5',
          labelList: ['565', '607', '475', '740', '633', '885'],
          labelAcc: [98.0, 96.0, 94.0, 12.0, 10.0, 10.0]
        }
      ]
    },
    {
      label: 'MISC',
      modelsInfo: [
        {
          model: 'mobilenet_v2',
          labelList: ['927', '933', '940', '969', '999', '961'],
          labelAcc: [92.0, 90.0, 88.0, 36.0, 36.0, 34.0]
        },
        {
          model: 'alexnet',
          labelList: ['946', '927', '938', '961', '968', '999'],
          labelAcc: [90.0, 90.0, 88.0, 20.0, 20.0, 14.0]
        },
        {
          model: 'resnet18',
          labelList: ['937', '927', '946', '969', '968', '961'],
          labelAcc: [90.0, 90.0, 88.0, 38.0, 34.0, 30.0]
        },
        {
          model: 'resnet34',
          labelList: ['927', '933', '937', '968', '947', '961'],
          labelAcc: [90.0, 90.0, 90.0, 40.0, 34.0, 32.0]
        },
        {
          model: 'resnet50',
          labelList: ['933', '927', '938', '999', '947', '968'],
          labelAcc: [94.0, 92.0, 92.0, 42.0, 38.0, 38.0]
        },
        {
          model: 'resnet101',
          labelList: ['927', '933', '936', '968', '947', '961'],
          labelAcc: [94.0, 94.0, 92.0, 44.0, 38.0, 36.0]
        },
        {
          model: 'resnet152',
          labelList: ['927', '933', '971', '968', '947', '923'],
          labelAcc: [94.0, 92.0, 90.0, 42.0, 40.0, 38.0]
        },
        {
          model: 'densenet121',
          labelList: ['946', '937', '927', '968', '947', '961'],
          labelAcc: [94.0, 94.0, 94.0, 38.0, 34.0, 32.0]
        },
        {
          model: 'densenet161',
          labelList: ['933', '927', '937', '947', '961', '968'],
          labelAcc: [98.0, 92.0, 90.0, 40.0, 38.0, 36.0]
        },
        {
          model: 'densenet169',
          labelList: ['927', '933', '937', '961', '947', '999'],
          labelAcc: [96.0, 94.0, 94.0, 40.0, 36.0, 36.0]
        },
        {
          model: 'densenet201',
          labelList: ['927', '936', '946', '947', '968', '961'],
          labelAcc: [98.0, 92.0, 92.0, 42.0, 42.0, 34.0]
        },
        {
          model: 'squeezenet1_1',
          labelList: ['927', '937', '946', '961', '999', '968'],
          labelAcc: [90.0, 88.0, 86.0, 24.0, 18.0, 16.0]
        },
        {
          model: 'shufflenet_v2_x0_5',
          labelList: ['927', '933', '946', '968', '923', '999'],
          labelAcc: [92.0, 88.0, 88.0, 26.0, 24.0, 22.0]
        }
      ]
    },
    {
      label: 'natural object',
      modelsInfo: [
        {
          model: 'mobilenet_v2',
          labelList: ['984', '988', '989', '977', '987', '998'],
          labelAcc: [98.0, 96.0, 94.0, 62.0, 46.0, 42.0]
        },
        {
          model: 'alexnet',
          labelList: ['984', '955', '989', '949', '987', '998'],
          labelAcc: [94.0, 90.0, 86.0, 50.0, 46.0, 38.0]
        },
        {
          model: 'resnet18',
          labelList: ['984', '988', '955', '977', '998', '987'],
          labelAcc: [98.0, 94.0, 94.0, 58.0, 48.0, 34.0]
        },
        {
          model: 'resnet34',
          labelList: ['984', '989', '988', '977', '987', '998'],
          labelAcc: [98.0, 96.0, 96.0, 64.0, 50.0, 44.0]
        },
        {
          model: 'resnet50',
          labelList: ['984', '989', '953', '977', '998', '987'],
          labelAcc: [100.0, 96.0, 96.0, 64.0, 50.0, 48.0]
        },
        {
          model: 'resnet101',
          labelList: ['989', '988', '984', '977', '998', '987'],
          labelAcc: [98.0, 98.0, 98.0, 60.0, 50.0, 44.0]
        },
        {
          model: 'resnet152',
          labelList: ['988', '990', '989', '987', '949', '998'],
          labelAcc: [100.0, 98.0, 98.0, 54.0, 54.0, 46.0]
        },
        {
          model: 'densenet121',
          labelList: ['988', '948', '990', '949', '987', '998'],
          labelAcc: [96.0, 94.0, 94.0, 62.0, 52.0, 50.0]
        },
        {
          model: 'densenet161',
          labelList: ['989', '988', '990', '949', '998', '987'],
          labelAcc: [98.0, 98.0, 96.0, 58.0, 58.0, 46.0]
        },
        {
          model: 'densenet169',
          labelList: ['990', '956', '984', '998', '977', '987'],
          labelAcc: [98.0, 96.0, 96.0, 60.0, 54.0, 48.0]
        },
        {
          model: 'densenet201',
          labelList: ['984', '989', '953', '998', '949', '987'],
          labelAcc: [100.0, 96.0, 96.0, 62.0, 58.0, 48.0]
        },
        {
          model: 'squeezenet1_1',
          labelList: ['955', '984', '990', '949', '987', '998'],
          labelAcc: [88.0, 86.0, 82.0, 52.0, 42.0, 34.0]
        },
        {
          model: 'shufflenet_v2_x0_5',
          labelList: ['984', '948', '955', '949', '998', '987'],
          labelAcc: [94.0, 88.0, 88.0, 56.0, 54.0, 32.0]
        }
      ]
    },
    {
      label: 'geological formation',
      modelsInfo: [
        {
          model: 'mobilenet_v2',
          labelList: ['974', '980', '979', '970', '975', '978'],
          labelAcc: [94.0, 82.0, 80.0, 46.0, 42.0, 36.0]
        },
        {
          model: 'alexnet',
          labelList: ['974', '979', '980', '970', '978', '976'],
          labelAcc: [90.0, 74.0, 68.0, 40.0, 38.0, 38.0]
        },
        {
          model: 'resnet18',
          labelList: ['974', '979', '980', '970', '975', '978'],
          labelAcc: [96.0, 70.0, 68.0, 50.0, 42.0, 40.0]
        },
        {
          model: 'resnet34',
          labelList: ['974', '980', '979', '970', '975', '978'],
          labelAcc: [92.0, 88.0, 72.0, 52.0, 48.0, 42.0]
        },
        {
          model: 'resnet50',
          labelList: ['974', '980', '973', '970', '975', '978'],
          labelAcc: [96.0, 86.0, 76.0, 58.0, 46.0, 38.0]
        },
        {
          model: 'resnet101',
          labelList: ['974', '980', '979', '970', '975', '978'],
          labelAcc: [94.0, 90.0, 76.0, 60.0, 48.0, 46.0]
        },
        {
          model: 'resnet152',
          labelList: ['974', '980', '973', '976', '970', '978'],
          labelAcc: [98.0, 86.0, 78.0, 56.0, 56.0, 38.0]
        },
        {
          model: 'densenet121',
          labelList: ['974', '980', '979', '976', '970', '978'],
          labelAcc: [96.0, 80.0, 74.0, 54.0, 50.0, 42.0]
        },
        {
          model: 'densenet161',
          labelList: ['974', '980', '973', '975', '976', '978'],
          labelAcc: [98.0, 92.0, 74.0, 60.0, 58.0, 42.0]
        },
        {
          model: 'densenet169',
          labelList: ['974', '980', '979', '976', '978', '970'],
          labelAcc: [98.0, 84.0, 68.0, 54.0, 50.0, 48.0]
        },
        {
          model: 'densenet201',
          labelList: ['974', '980', '979', '976', '975', '978'],
          labelAcc: [96.0, 90.0, 76.0, 56.0, 54.0, 48.0]
        },
        {
          model: 'squeezenet1_1',
          labelList: ['974', '980', '973', '976', '975', '978'],
          labelAcc: [90.0, 66.0, 66.0, 48.0, 40.0, 30.0]
        },
        {
          model: 'shufflenet_v2_x0_5',
          labelList: ['974', '980', '977', '976', '975', '978'],
          labelAcc: [94.0, 78.0, 62.0, 54.0, 30.0, 24.0]
        }
      ]
    },
    {
      label: 'person',
      modelsInfo: [
        {
          model: 'mobilenet_v2',
          labelList: ['983', '981', '982'],
          labelAcc: [84.0, 80.0, 72.0]
        },
        {
          model: 'alexnet',
          labelList: ['983', '981', '982'],
          labelAcc: [74.0, 60.0, 56.0]
        },
        {
          model: 'resnet18',
          labelList: ['983', '981', '982'],
          labelAcc: [86.0, 76.0, 70.0]
        },
        {
          model: 'resnet34',
          labelList: ['983', '981', '982'],
          labelAcc: [82.0, 80.0, 74.0]
        },
        {
          model: 'resnet50',
          labelList: ['983', '982', '981'],
          labelAcc: [86.0, 78.0, 76.0]
        },
        {
          model: 'resnet101',
          labelList: ['983', '981', '982'],
          labelAcc: [84.0, 80.0, 78.0]
        },
        {
          model: 'resnet152',
          labelList: ['983', '981', '982'],
          labelAcc: [88.0, 82.0, 78.0]
        },
        {
          model: 'densenet121',
          labelList: ['983', '981', '982'],
          labelAcc: [84.0, 76.0, 68.0]
        },
        {
          model: 'densenet161',
          labelList: ['983', '981', '982'],
          labelAcc: [90.0, 76.0, 72.0]
        },
        {
          model: 'densenet169',
          labelList: ['983', '981', '982'],
          labelAcc: [86.0, 72.0, 66.0]
        },
        {
          model: 'densenet201',
          labelList: ['983', '982', '981'],
          labelAcc: [90.0, 86.0, 78.0]
        },
        {
          model: 'squeezenet1_1',
          labelList: ['983', '981', '982'],
          labelAcc: [80.0, 64.0, 52.0]
        },
        {
          model: 'shufflenet_v2_x0_5',
          labelList: ['983', '981', '982'],
          labelAcc: [74.0, 70.0, 56.0]
        }
      ]
    },
    {
      label: 'plant',
      modelsInfo: [
        {
          model: 'mobilenet_v2',
          labelList: ['986', '985'],
          labelAcc: [100.0, 96.0]
        },
        {
          model: 'alexnet',
          labelList: ['986', '985'],
          labelAcc: [100.0, 94.0]
        },
        {
          model: 'resnet18',
          labelList: ['986', '985'],
          labelAcc: [100.0, 94.0]
        },
        {
          model: 'resnet34',
          labelList: ['986', '985'],
          labelAcc: [100.0, 96.0]
        },
        {
          model: 'resnet50',
          labelList: ['986', '985'],
          labelAcc: [100.0, 94.0]
        },
        {
          model: 'resnet101',
          labelList: ['986', '985'],
          labelAcc: [100.0, 98.0]
        },
        {
          model: 'resnet152',
          labelList: ['986', '985'],
          labelAcc: [100.0, 96.0]
        },
        {
          model: 'densenet121',
          labelList: ['986', '985'],
          labelAcc: [100.0, 96.0]
        },
        {
          model: 'densenet161',
          labelList: ['986', '985'],
          labelAcc: [100.0, 96.0]
        },
        {
          model: 'densenet169',
          labelList: ['986', '985'],
          labelAcc: [100.0, 100.0]
        },
        {
          model: 'densenet201',
          labelList: ['986', '985'],
          labelAcc: [100.0, 98.0]
        },
        {
          model: 'squeezenet1_1',
          labelList: ['986', '985'],
          labelAcc: [100.0, 90.0]
        },
        {
          model: 'shufflenet_v2_x0_5',
          labelList: ['986', '985'],
          labelAcc: [100.0, 96.0]
        }
      ]
    },
    {
      label: 'fungus',
      modelsInfo: [
        {
          model: 'mobilenet_v2',
          labelList: ['995', '993', '991', '994', '996', '997'],
          labelAcc: [100.0, 96.0, 96.0, 84.0, 82.0, 78.0]
        },
        {
          model: 'alexnet',
          labelList: ['993', '995', '991', '996', '994', '997'],
          labelAcc: [96.0, 92.0, 92.0, 70.0, 64.0, 56.0]
        },
        {
          model: 'resnet18',
          labelList: ['995', '993', '991', '992', '994', '997'],
          labelAcc: [100.0, 96.0, 94.0, 82.0, 78.0, 70.0]
        },
        {
          model: 'resnet34',
          labelList: ['995', '993', '991', '992', '996', '997'],
          labelAcc: [100.0, 96.0, 96.0, 86.0, 82.0, 70.0]
        },
        {
          model: 'resnet50',
          labelList: ['995', '993', '991', '994', '992', '997'],
          labelAcc: [100.0, 96.0, 96.0, 86.0, 84.0, 72.0]
        },
        {
          model: 'resnet101',
          labelList: ['995', '993', '991', '996', '992', '997'],
          labelAcc: [100.0, 96.0, 94.0, 86.0, 86.0, 72.0]
        },
        {
          model: 'resnet152',
          labelList: ['995', '993', '991', '994', '992', '997'],
          labelAcc: [100.0, 96.0, 94.0, 90.0, 86.0, 72.0]
        },
        {
          model: 'densenet121',
          labelList: ['995', '993', '996', '992', '994', '997'],
          labelAcc: [100.0, 96.0, 94.0, 86.0, 84.0, 68.0]
        },
        {
          model: 'densenet161',
          labelList: ['995', '993', '991', '994', '992', '997'],
          labelAcc: [100.0, 96.0, 96.0, 86.0, 80.0, 62.0]
        },
        {
          model: 'densenet169',
          labelList: ['995', '991', '993', '994', '992', '997'],
          labelAcc: [100.0, 96.0, 94.0, 90.0, 86.0, 72.0]
        },
        {
          model: 'densenet201',
          labelList: ['995', '993', '991', '996', '992', '997'],
          labelAcc: [100.0, 98.0, 96.0, 88.0, 86.0, 76.0]
        },
        {
          model: 'squeezenet1_1',
          labelList: ['995', '991', '993', '996', '994', '997'],
          labelAcc: [96.0, 94.0, 92.0, 78.0, 72.0, 64.0]
        },
        {
          model: 'shufflenet_v2_x0_5',
          labelList: ['995', '993', '991', '996', '994', '997'],
          labelAcc: [96.0, 92.0, 86.0, 74.0, 74.0, 62.0]
        }
      ]
    }
  ],
  barModelInfo: [
    {
      model: 'mobilenet_v2',
      labelList: ['986', '565', '102', '836', '782', '885'],
      labelAcc: [100.0, 100.0, 100.0, 14.0, 10.0, 10.0]
    },
    {
      model: 'alexnet',
      labelList: ['90', '986', '376', '813', '836', '885'],
      labelAcc: [100.0, 100.0, 98.0, 6.0, 6.0, 6.0]
    },
    {
      model: 'resnet18',
      labelList: ['364', '995', '333', '282', '620', '836'],
      labelAcc: [100.0, 100.0, 100.0, 12.0, 12.0, 8.0]
    },
    {
      model: 'resnet34',
      labelList: ['255', '333', '995', '620', '818', '885'],
      labelAcc: [100.0, 100.0, 100.0, 14.0, 14.0, 10.0]
    },
    {
      model: 'resnet50',
      labelList: ['135', '259', '255', '240', '638', '885'],
      labelAcc: [100.0, 100.0, 100.0, 20.0, 18.0, 18.0]
    },
    {
      model: 'resnet101',
      labelList: ['13', '139', '376', '885', '282', '782'],
      labelAcc: [100.0, 100.0, 100.0, 18.0, 18.0, 16.0]
    },
    {
      model: 'resnet152',
      labelList: ['93', '986', '13', '282', '782', '885'],
      labelAcc: [100.0, 100.0, 100.0, 24.0, 22.0, 22.0]
    },
    {
      model: 'densenet121',
      labelList: ['9', '685', '376', '885', '836', '782'],
      labelAcc: [100.0, 100.0, 100.0, 14.0, 14.0, 12.0]
    },
    {
      model: 'densenet161',
      labelList: ['344', '874', '148', '782', '282', '638'],
      labelAcc: [100.0, 100.0, 100.0, 22.0, 20.0, 20.0]
    },
    {
      model: 'densenet169',
      labelList: ['466', '554', '995', '620', '282', '782'],
      labelAcc: [100.0, 100.0, 100.0, 18.0, 18.0, 14.0]
    },
    {
      model: 'densenet201',
      labelList: ['984', '800', '9', '885', '818', '782'],
      labelAcc: [100.0, 100.0, 100.0, 22.0, 22.0, 18.0]
    },
    {
      model: 'squeezenet1_1',
      labelList: ['986', '376', '340', '784', '838', '885'],
      labelAcc: [100.0, 96.0, 96.0, 10.0, 10.0, 10.0]
    },
    {
      model: 'shufflenet_v2_x0_5',
      labelList: ['275', '986', '565', '782', '885', '633'],
      labelAcc: [100.0, 100.0, 98.0, 12.0, 10.0, 10.0]
    }
  ]
}
