import 'package:flutter/material.dart';
import 'package:src/presentacio/controladorPresentacio.dart';
import 'package:src/presentacio/screens/afegirSimptomes.dart';
import 'package:src/presentacio/screens/forum.dart';
import 'package:src/presentacio/screens/grafics.dart';

class Aula extends StatefulWidget {
  final ControladorPresentacio controladorPresentacio;

  const Aula({Key? key, required this.controladorPresentacio})
      : super(key: key);

  @override
  State<Aula> createState() => _Aula(controladorPresentacio);
}

class _Aula extends State<Aula> {
  late ControladorPresentacio _controladorPresentacio;
  late int index_marcat;

  _Aula(ControladorPresentacio controladorPresentacio) {
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

  Widget retornaPantalla() {
    if (index_marcat == 0) {
      return Grafics();
    } else if (index_marcat == 1) {
      return AfegirSimptomes();
    }
    return Forum();
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
                  Text(
                    'Aula: nombre aula',
                    style: TextStyle(
                      fontSize: 30,
                      fontWeight: FontWeight.bold,
                      color: Color.fromRGBO(8, 72, 135, 1),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),
            retornaPantalla(),
          ],
        ),
      ),
      bottomNavigationBar: MenuInferior(),
    );
  }

  void _onItemTapped(int index) {
    setState(() {
      index_marcat = index;
    });
  }

  Widget MenuInferior() {
    return SizedBox(
      child: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.auto_graph),
            label: 'Gràfics',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.mode_edit),
            label: 'Formulari',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.mode_comment_rounded),
            label: 'Fórum',
          ),
        ],
        currentIndex: index_marcat,
        backgroundColor: Color.fromRGBO(73, 160, 120, 1),
        selectedItemColor: Colors.white,
        onTap: _onItemTapped,
      ),
    );
  }
}
