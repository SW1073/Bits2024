/*import 'package:flutter/material.dart';

class MenuInferior extends StatefulWidget {
  const MenuInferior({super.key});

  @override
  State<MenuInferior> createState() => _MenuInferior();
}

class _MenuInferior extends State<MenuInferior> {
  int _selectedIndex = 0;
  static const TextStyle optionStyle =
      TextStyle(fontSize: 30, fontWeight: FontWeight.bold);
  static const List<Widget> _widgetOptions = <Widget>[
    Text(
      'Index 0: Home',
      style: optionStyle,
    ),
    Text(
      'Index 1: Business',
      style: optionStyle,
    ),
    Text(
      'Index 2: School',
      style: optionStyle,
    ),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
        child: BottomNavigationBar(
      items: const <BottomNavigationBarItem>[
        BottomNavigationBarItem(
          icon: Icon(Icons.home),
          label: 'Gràfics',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.business),
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.school),
          label: 'Fórum',
        ),
      ],
      currentIndex: _selectedIndex,
      backgroundColor: Color.fromRGBO(44, 246, 179, 1),
      selectedItemColor: Colors.white,
      onTap: _onItemTapped,
    ));
  }
}*/
