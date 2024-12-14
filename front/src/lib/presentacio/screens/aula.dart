import 'package:flutter/material.dart';
import 'package:src/presentacio/controladorPresentacio.dart';
import 'package:src/presentacio/widgets/menuInferior.dart';

class Aula extends StatefulWidget {
  final ControladorPresentacio controladorPresentacio;

  const Aula({Key? key, required this.controladorPresentacio})
      : super(key: key);

  @override
  State<Aula> createState() => _Aula(controladorPresentacio);
}

class _Aula extends State<Aula> {
  late ControladorPresentacio _controladorPresentacio;

  _Aula(ControladorPresentacio controladorPresentacio) {
    _controladorPresentacio = controladorPresentacio;
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
                    width: 20,
                  ),
                  Text(
                    'Aula',
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
            Expanded(
              child: ListView.builder(
                itemCount: 4,
                itemBuilder: (context, index) {
                  return Container(
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
                          'Gràfic',
                          style: TextStyle(
                            fontSize: 20,
                            fontWeight: FontWeight.bold,
                            color: Color.fromRGBO(8, 72, 135, 1),
                          ),
                        ),
                        const SizedBox(height: 10),
                      ],
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: MenuInferior(),
    );
  }
}
