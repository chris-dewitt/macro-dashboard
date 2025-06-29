import backtrader as bt

class MacroSentEventStrategy(bt.Strategy):
    params = dict(regime_col='regime', signal_col='signal')

    def __init__(self):
        self.regime = self.datas[0].lines[self.params.regime_col]
        self.signal = self.datas[0].lines[self.params.signal_col]

    def next(self):
        if not self.position:
            if self.regime[0] == 1 and self.signal[0] > 0:
                self.buy()
        else:
            if self.signal[0] < 0:
                self.close()
