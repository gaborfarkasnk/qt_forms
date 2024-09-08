import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

ApplicationWindow{
                width: 600
                height: 600
                title: "My form"
                visible: true
                Material.theme: Material.Dark
                Material.accent: Material.LightBlue

                ColumnLayout{}

                Button{
                    text: "button"
                    x: 100
                    y: 100
                    }
                Button{
                    text: "button2"
                    x: 200
                    y: 100
                    }
                Text{
                    text: "I am a label"
                    
                }
                TextField{
                    placeholderText: "Name"
                    y: 50
                }
                TextField{
                    placeholderText: "Email"
                    y: 150
                }   
                TextField{
                    placeholderText: "Address"
                    y: 250
                }   
                           
}