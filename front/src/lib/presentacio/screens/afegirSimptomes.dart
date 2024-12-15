import 'package:flutter/material.dart';

class AfegirSimptomes extends StatefulWidget {
  const AfegirSimptomes({super.key});

  @override
  State<AfegirSimptomes> createState() => _AfegirSimptomes();
}

class _AfegirSimptomes extends State<AfegirSimptomes> {
  final List<String> _options = [
    'Mal de panxa',
    'Calfreds',
    'Mal de cap',
    'Mal de coll',
    'Mocs',
    'Nas tapat',
    'Esternut',
    'Vomits',
    'Tos',
    'Altres'
  ];

  late List<String> simptomes = [];

  String? _selectedOption;
  late String _selectedRadio = "Bé";

  void eliminarSimptoma(index) {
    setState(() {
      simptomes.removeAt(index);
    });
  }

  void enviarFormulari() {
    //cridar a funció per enviar formulari a backend
    //data del dia d'avui
    //agafa els simptomes
    //agafa el valor de radio -> ficar dins de simptomes
    setState(() {
      simptomes = [];
      _selectedRadio = "Bé";
      _selectedOption = null;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        children: [
          SizedBox(
            child: Text(
              'Formulari',
              style: TextStyle(
                color: Color.fromRGBO(8, 72, 135, 1),
                fontWeight: FontWeight.bold,
                fontSize: 35,
              ),
            ),
          ),
          SizedBox(
            height: 50,
          ),
          Container(
            padding: EdgeInsets.only(
              left: 15,
              right: 15,
            ),
            child: Row(
              children: [
                Text(
                  'Símptomes: ',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 20,
                  ),
                ),
                SizedBox(
                  width: 15,
                ),
                DropdownButton<String>(
                  value: _selectedOption,
                  hint: Text(
                    'Selecciona una opció ',
                    style: TextStyle(
                      fontSize: 20,
                    ),
                  ),
                  items: _options.map((String option) {
                    return DropdownMenuItem<String>(
                      value: option,
                      child: Text(option),
                    );
                  }).toList(),
                  onChanged: (String? newValue) {
                    setState(() {
                      _selectedOption = newValue;
                      simptomes.contains(_selectedOption)
                          ? ''
                          : simptomes.add(_selectedOption!);
                    });
                  },
                ),
              ],
            ),
          ),
          SizedBox(
            height: 20,
          ),
          SizedBox(
            height: 420,
            child: Expanded(
              child: simptomes.isNotEmpty
                  ? simptomesRegistrats()
                  : Text(
                      '- No has seleccionat cap símptoma encara - ',
                      style: TextStyle(fontSize: 22),
                    ),
            ),
          ),
          SizedBox(
            height: 10,
          ),
          Row(
            children: [
              Text(
                'Estat : ',
                style: TextStyle(
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Expanded(
                child: RadioListTile<String>(
                  value: "Bé",
                  groupValue: _selectedRadio,
                  title: const Text("Bé"),
                  onChanged: (value) {
                    setState(() {
                      _selectedRadio = value!;
                    });
                  },
                ),
              ),
              Expanded(
                child: RadioListTile<String>(
                  value: "Regular",
                  groupValue: _selectedRadio,
                  title: const Text("Regular"),
                  onChanged: (value) {
                    setState(() {
                      _selectedRadio = value!;
                    });
                  },
                ),
              ),
              Expanded(
                child: RadioListTile<String>(
                  value: "Malament",
                  groupValue: _selectedRadio,
                  title: const Text("Malament"),
                  onChanged: (value) {
                    setState(() {
                      _selectedRadio = value!;
                    });
                  },
                ),
              ),
            ],
          ),
          SizedBox(
            height: 10,
          ),
          Container(
            padding: EdgeInsets.all(8),
            child: TextButton(
              onPressed: enviarFormulari,
              style: TextButton.styleFrom(
                padding: EdgeInsets.all(16),
                backgroundColor: Color.fromRGBO(8, 72, 135, 1),
              ),
              child: const Text(
                'Enviar',
                style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 20,
                ),
              ),
            ),
          )
        ],
      ),
    );
  }

  Widget simptomesRegistrats() {
    return ListView.builder(
      itemCount: simptomes.length,
      itemBuilder: (context, index) {
        return GestureDetector(
          onTap: () {
            eliminarSimptoma(index);
          },
          child: Container(
            margin: const EdgeInsets.symmetric(
              vertical: 10,
              horizontal: 40,
            ),
            padding: const EdgeInsets.all(16.0),
            decoration: BoxDecoration(
              color: Color.fromRGBO(219, 212, 211, 1),
              borderRadius: BorderRadius.circular(12.0),
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  simptomes[index],
                  style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    color: Color.fromRGBO(8, 72, 135, 1),
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}
