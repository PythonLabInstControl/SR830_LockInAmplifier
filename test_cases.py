# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 11:22:20 2014
@author: Veronika Schrenk

This script implements test scenarios for the stanford_SR830_modified.liaSR830 class
in the same order as the methods are implemented in the stanford_SR830_modified.liaSR830 class
Each test scenario is separated from the other ones through a new line
"""
import stanford_SR830_modified

x = stanford_SR830_modified.liaSR830();

#print(x.check_instr());

#x.correct_phaseshift();???

#print(x.ConvertiToTimeconstant(5));

#print(x.ConvertTimeconstantToi(0.03))

#x.SetSensitivityLIA(10e-6);

#x.SendString("freq 800")

#print(x.getR())

#print(x.getPhi())

#print(x.getSens());

#print(x.getF());

#x.SerialPollDiagnostic();

#x.SetRefRms(0.35)
#print(x.GetRefRms());

#x.SetRefFreq(500)
#print(x.GetRefFreq())

#x.SetRefPhas(541)
#print(x.GetRefPhas())

#x.SetRefMode(1);
#print(x.GetRefMode());

#x.SetRefHarm(5);
#print(x.GetRefHarm());

#x.SetInputConfig(3);
#print(x.GetInputConfig());

#x.SetGNDConfig(0);
#print(x.GetGNDConfig());

#x.SetInputCoupling(0);
#print(x.GetInputCoupling());

#x.SetLineNotch(3);
#print(x.GetLineNotch());

#x.SetSens(5);
#print(x.GetSens());

#x.SetReserve(2);
#print(x.GetReserve());

#x.SetTimeConst(13);
#print(x.GetTimeConst());

#x.SetSlope(3);
#print(x.GetSlope());

#x.SetSyncFilter(1);
#print(x.GetSyncFilter());

#x.SetDisplay(2,1);
#print(x.GetDisplay(2));

#x.SetInterface()
#print(x.GetInterface());

#x.SetDisableRemoteLockoutState(False);

#x.SetKlickOn(True);
#print(x.GetKlickOn())

#x.SetAlarm(True);
#print(x.GetAlarm());

#x.SaveSettings();

#x.ReactivateSettings();

#x.SetAutoGain();

#print(x.GetFrontOutputSource(1));
#x.SetFrontOutputSource(1, 0);
#print(x.GetFrontOutputSource(1));

#x.SetOutputOffsetAndExpand('X', 20, 0);
#print(x.GetOutputOffsetAndExpand(1));

#x.SetAutoReserve();

#x.SetAutoPhase();

#x.SetAutoOffset(3);

#x.SetDataSampleRate();
#print(x.GetDataSampleRate());

#x.SetEndOfBuffer(0);
#print(x.GetEndOfBuffer());

#x.Trigger();

#x.SetTriggerStartMode(1);
#print(x.GetTriggerStartMode());

#x.Start();
#x.Pause();

#x.SetTriggerSlope(1);
#print(x.GetTriggerSlope());

#x.Reset();

#x.ResetDataBuffers();

#print(x.GetSelectedOutput(3));

#print(x.GetSelectedDisplayValue(2));

#print(x.SNAP(10, 11, 3,4,6,7));

#print(x.GetAuxValue(3));

#print(x.GetOccupiedBuffer());

x.close();