import 'package:flutter/material.dart';
import 'package:src/presentacio/controladorPresentacio.dart';
import 'package:src/presentacio/screens/afegirSimptomes.dart';
import 'package:src/presentacio/screens/forum.dart';
import 'package:src/presentacio/screens/grafics.dart';

class AfegirAules extends StatefulWidget {
  final ControladorPresentacio controladorPresentacio;

  const AfegirAules({Key? key, required this.controladorPresentacio})
      : super(key: key);

  @override
  State<AfegirAules> createState() => _AfegirAules(controladorPresentacio);
}

class _AfegirAules extends State<AfegirAules> {
  late ControladorPresentacio _controladorPresentacio;
  late int index_marcat;

  _AfegirAules(ControladorPresentacio controladorPresentacio) {
    _controladorPresentacio = controladorPresentacio;
    index_marcat = 0;
  }

  @override
  void initState() {
    super.initState();
  }

  // blau fosc -> Color.fromRGBO(8, 72, 135, 1)
  // aquamarina -> Color.fromRGBO(44, 246, 179, 1)
  // verd -> Color.fromRGBO(73, 160, 120, 1)
  // gris -> Color.fromRGBO(219, 212, 211, 1)

  void anarAMevesAules() {
    return _controladorPresentacio.mostraMevesAules(context);
  }

  void afegirAula() {
    print('afegir');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              margin: const EdgeInsets.symmetric(
                vertical: 10,
                horizontal: 20,
              ),
              child: Row(
                children: [
                  IconButton(
                    onPressed: anarAMevesAules,
                    icon: Icon(
                      Icons.arrow_back,
                      color: Color.fromRGBO(8, 72, 135, 1),
                    ),
                  ),
                  SizedBox(
                    width: 30,
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),
            Center(
              child: Text(
                "Afegir aula",
                style: TextStyle(
                  color: Color.fromRGBO(8, 72, 135, 1),
                  fontWeight: FontWeight.bold,
                  fontSize: 35,
                ),
              ),
            ),
            /*Expanded(
              child: Container(
                child: Column(
                  children: [
                    ListTile(
                      leading: Text('Provincia: '),
                      title: ,
                    )
                  ],
                ),
              ),
            ),*/
            Container(
              padding: EdgeInsets.all(8),
              alignment: Alignment.bottomRight,
              child: TextButton(
                onPressed: afegirAula,
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
      ),
    );
  }
}
