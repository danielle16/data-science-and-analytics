Attribute VB_Name = "Module1"
Sub stock_analysis()
    Dim rowCount As Long
    Dim percentChanged As Long
    Dim days As Integer
    Dim dailyChanged As Double
    Dim averageChanged As Double
    Dim change As Long
    Dim j As Integer
    Dim index As Long
    Dim total As Double
    Dim i As Long


    Range("I1").Value = "Ticker"
    Range("J1").Value = "Yearly Change"
    Range("K1").Value = "Percent Change"
    Range("L1").Value = "Total Stock Volume"
    Range("P1").Value = "Ticker"
    Range("Q1").Value = "Value"
    Range("O2").Value = "Greatest % Increase"
    Range("O3").Value = "Greatest % Decrease"
    Range("O4").Value = "Greatest Total Volume"

    j = 1
    total = 0
    change = 0
    index = 2


    rowCount = Cells(Rows.Count, "A").End(xlUp).Row
    
    For i = 2 To rowCount
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            total = total + Cells(i, 7).Value
            
            change = (Cells(i, 6) - Cells(index, 3))
            percentChange = Round((change / Cells(index, 3) * 100), 2)

            Cells(j + 1, "I").Value = Cells(i, 1).Value
            Cells(j + 1, "L").Value = total
            Cells(j + 1, "J").Value = change
            Cells(j + 1, "K").Value = percentChange

            If Cells(j + 1, "J").Value < 0 Then
                 Cells(j + 1, "J").Interior.ColorIndex = 3
            ElseIf Cells(j + 1, "J").Value > 0 Then
                Cells(j + 1, "J").Interior.ColorIndex = 4
            Else
            End If
            j = j + 1
            total = 0
            index = i + 1
        Else
            total = total + Cells(i, 7).Value
        End If
    Next i
            
    
    
    
End Sub

