Imports System.Diagnostics.Eventing.Reader
Imports System.Net.NetworkInformation

Public Class Form1
    Private Sub btnCompute_Click(sender As Object, e As EventArgs) Handles btnCompute.Click
        Dim i As Integer = 1
        Dim pie As Double = 3.142
        Dim rc As Double
        Dim sa As Double
        Dim wb As Double
        Dim hc As Double
        Dim wl As Double
        Dim wh As Double
        Dim volume As Double
        Dim mass As Double
        Dim density As Double
        Dim Icount As Integer

        Icount = InputBox("How many models ?")

        For i = 1 To iCount
            rc = InputBox("enter radius of the cylinder  ")
            hc = InputBox("enter height of the cylinder  ")
            wb = InputBox(" enter width of the box ")
            wl = InputBox("enter the length of the box ")
            wh = InputBox("enter the height of the box ")
            mass = InputBox("enter mass of the model")
            volume = wl * wb * hc + pie * rc ^ 2 * hc + 2 / 3 * pie * rc ^ 3
            sa = 2 * ((wl * wb) + (wl * wh) + (wb * wh)) + pie * rc + 2 * pie * rc ^ 2
            density = mass / volume

            MessageBox.Show("SPECYBOX MODEL" &
                                vbNewLine & "radius of the cylinder  :" & rc &
                                vbNewLine & "box length = " & wl &
                                vbNewLine & " box width =" & wb &
                                vbNewLine & "box height  =  " & hc &
                                vbNewLine & "cylinder radius =   " & rc &
                                vbNewLine & "volume of the model is " & volume &
                                vbNewLine & " its total sa is " & sa &
                                vbNewLine & "density is" & density)
            If (density >= 25) Then
                MessageBox.Show("super density")
            ElseIf (density >= 20 And density < 25) Then
                MessageBox.Show("high density")
            ElseIf (density >= 15 And density < 20) Then
                MessageBox.Show("medium density")
            ElseIf (density >= 10 And density < 15) Then
                MessageBox.Show("acceptable low density")
            Else
                MessageBox.Show("unacceptable low density")
            End If
        Next









    End Sub

    Private Sub PrintPreviewControl1_Click(sender As Object, e As EventArgs)

    End Sub
End Class
