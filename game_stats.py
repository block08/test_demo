# 跟踪游戏的统计信息
class GameStats():
    # 初始化统计信息
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        # 在任何情况下都不应重置最高得分
        self.game_score = 0
        self.collide = False
        self.stag = 0
