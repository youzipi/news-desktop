/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50535
Source Host           : 127.0.0.1:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50535
File Encoding         : 65001

Date: 2014-08-12 16:56:14
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_category
-- ----------------------------
DROP TABLE IF EXISTS `t_category`;
CREATE TABLE `t_category` (
  `cid` int(11) NOT NULL AUTO_INCREMENT COMMENT '分类编号',
  `title` varchar(5) NOT NULL COMMENT '分类名称',
  `sequnce` int(11) DEFAULT '0' COMMENT '序列',
  `deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0:false;1:true',
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_category
-- ----------------------------
INSERT INTO `t_category` VALUES ('1', '焦点', '0', '0');
INSERT INTO `t_category` VALUES ('2', '国内', '0', '0');
INSERT INTO `t_category` VALUES ('3', '国际', '0', '0');
INSERT INTO `t_category` VALUES ('4', '体育', '0', '0');
INSERT INTO `t_category` VALUES ('5', '文娱', '0', '0');
INSERT INTO `t_category` VALUES ('6', '科技', '0', '0');

-- ----------------------------
-- Table structure for t_comment
-- ----------------------------
DROP TABLE IF EXISTS `t_comment`;
CREATE TABLE `t_comment` (
  `cid` int(11) NOT NULL AUTO_INCREMENT COMMENT '评论编号',
  `nid` int(11) NOT NULL COMMENT '新闻编号',
  `ptime` varchar(20) CHARACTER SET utf8 NOT NULL COMMENT '评论时间',
  `region` varchar(20) CHARACTER SET utf8 NOT NULL DEFAULT '未知地区' COMMENT '发布人地区',
  `content` varchar(500) CHARACTER SET utf8 NOT NULL COMMENT '评论内容',
  `supportcount` int(11) NOT NULL DEFAULT '0' COMMENT '支持数',
  `opposecount` int(11) NOT NULL DEFAULT '0' COMMENT '反对数',
  `deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0:false;1:true',
  PRIMARY KEY (`cid`),
  KEY `FK_t_comment_t_news` (`nid`),
  CONSTRAINT `FK_t_comment_t_news` FOREIGN KEY (`nid`) REFERENCES `t_news` (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_comment
-- ----------------------------

-- ----------------------------
-- Table structure for t_news
-- ----------------------------
DROP TABLE IF EXISTS `t_news`;
CREATE TABLE `t_news` (
  `nid` int(11) NOT NULL AUTO_INCREMENT COMMENT '新闻编号',
  `cid` int(11) NOT NULL DEFAULT '1' COMMENT '新闻分类',
  `title` varchar(80) DEFAULT '无标题' COMMENT '新闻标题',
  `digest` varchar(100) DEFAULT '无概要' COMMENT '摘要',
  `body` text COMMENT '新闻内容',
  `source` varchar(20) DEFAULT '互联网' COMMENT '新闻来源',
  `ptime` varchar(20) DEFAULT NULL COMMENT '发布时间',
  `imgsrc` varchar(100) DEFAULT NULL COMMENT '新闻图片',
  `imgpath` text,
  `deleted` tinyint(1) DEFAULT '0' COMMENT '0:false;1:true',
  PRIMARY KEY (`nid`),
  KEY `FK_t_news_t_category` (`cid`),
  CONSTRAINT `FK_t_news_t_category` FOREIGN KEY (`cid`) REFERENCES `t_category` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_news
-- ----------------------------
INSERT INTO `t_news` VALUES ('1', '1', 'Kontakt.io发布支持WiFi的Cloud Beacon，除了低功耗蓝牙WiFi对Beacons也很重要 | 36氪', '无概要', '<p><img alt=\"\" src=\"E:/百度/3a2269.jpg\"/></p><p></p><p></p><p>一般情况下可以运用Beacons的场景有很多，例如当你在选购自行车时，就可以在靠近车把的地方获取目录推送，甚至直接通过手机支付应用对其进行购买。Beaconas还可以追踪用户在店内的浏览情况，收集此类数据有助于改善特定区域的产品布局，以便为客户提供更优异的购物体验。</p><p></p><p><img alt=\"\" src=\"E:/百度/807a9b.jpg\"/></p><p>Cloud Beacon已于今日开放预订，单件设备售价79美元，3件套装225美元。首批产品将于今年10月出货。</p><p></p><p></p><p class=\"single-post-author__bio\">Instagram●jingze/WeChat●DanielJingze</p><p>有了wifi这下比蓝牙好多了啊</p><p>我们在项目中已经应用了I Beacon，定位精准度在3m左右，范围到300米。其实其他网络功能都好实现，不是太大问题。关键是抗干扰能力，还有精准度吧。wifi200米覆盖这个事儿，其实没多大意思，这个是看人家wifi的功能，又不是触发和定位的技术。</p><p>微信公众平台：搜索“36氪”或扫描下面的二维码：</p><p></p><p></p><p>©2011-2014 36氪</p><p>京ICP备11027501号</p><p>京公网安备11010802012285号</p><p class=\"left\"><a href=\"/account/password/new\">忘记密码？</a></p><p></p><p></p><p><img alt=\"\" src=\"E:/百度/=wecha.jpg\"/></p>', '互联网', '2014-08-12', '=', 'W3UnRTovXHU3NjdlXHU1ZWE2LzNhMjI2OS5qcGcnLCB1J0U6L1x1NzY3ZVx1NWVhNi84MDdhOWIuanBnJywgdSdFOi9cdTc2N2VcdTVlYTYvPXdlY2hhLmpwZydd', '0');
