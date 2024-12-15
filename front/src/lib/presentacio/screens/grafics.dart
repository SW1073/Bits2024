import 'package:flutter/material.dart';

class Grafics extends StatefulWidget {
  const Grafics({super.key});

  @override
  State<Grafics> createState() => _Grafics();
}

class _Grafics extends State<Grafics> {
  List<String> nomGrafiques = [
    '../assets/Escola_Merce_Rodoreda_regular.png',
    '../assets/Escola_Merce_Rodoreda_malament.png'
  ];

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Column(
        children: [
          Text(
            "Gràfics de l'aula",
            style: TextStyle(
              color: Color.fromRGBO(8, 72, 135, 1),
              fontWeight: FontWeight.bold,
              fontSize: 35,
            ),
          ),
          SizedBox(
            height: 20,
          ),
          Expanded(
            child: ListView.builder(
              itemCount: 2,
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
                      Image.asset(
                        nomGrafiques[index],
                        width: 450,
                        height: 400,
                        fit: BoxFit.cover,
                      ),
                    ],
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
