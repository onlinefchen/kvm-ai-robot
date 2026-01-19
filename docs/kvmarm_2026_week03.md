# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2026-01-19 00:26:35

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 346
- **总 Thread 数**: 32
- **大型 Thread** (>20封): 4 个

### 分类分布

- **PATCH**: 26 threads (305 邮件)
- **RFC**: 4 threads (20 邮件)
- **Other**: 2 threads (21 邮件)

---

## 📌 PATCH

共 26 个 thread

---

### Thread 1: [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code

**📧 邮件数**: 110 | **👥 参与者**: 10 | **📅 开始时间**: Mon, 12 Jan 2026 16:58:27 +0000

#### 🤖 AI 总结

本邮件主题为“[PATCH v3 00/47] arm_mpam: 添加 KVM/arm64 和 resctrl 连接代码”，主要讨论了 ARM MPAM（内存系统资源分区和监控）与 KVM 和 resctrl 的集成。以下是对邮件讨论的总结：

1. **原始 patch/问题内容**：本次补丁系列的目标是将 ARM MPAM 的功能与 KVM 和 resctrl 结合，以支持资源监控和分配。补丁主要涉及 MPAM 的架构代码、KVM 支持以及 resctrl 的集成。

2. **之前讨论要点**：历史讨论中提到，MPAM 的设置在内核空间和用户空间之间共享，尽管这种策略有其优缺点。补丁的设计旨在简化 MPAM 的使用，使其能够在用户空间和内核空间之间有效地监控和分配资源。

3. **本周的新讨论、进展或结论**：本周的讨论集中在补丁的细节和实现上，包括：
   - 对 MPAM 相关寄存器的初始化和上下文切换的实现。
   - 增加了对 MBW（内存带宽）最小控制的支持，并确保在没有争用的情况下，带宽能够得到优先保障。
   - 引入了多项硬件缺陷的修复措施，以确保在特定硬件上正确配置 MPAM。
   - 讨论了如何处理 KVM 中的 MPAM 配置，确保虚拟机能够使用用户空间的 MPAM 设置。

参与者对补丁的各个方面进行了审查和反馈，部分补丁已获得“Reviewed-by”标记，显示出对该系列补丁的认可和支持。整体来看，此次补丁系列旨在增强 ARM MPAM 的功能，提升其在虚拟化和资源管理中的应用能力。

#### 📝 邮件列表

1. **[01-12 16:58]** [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[01-12 16:58]** [PATCH v3 01/47] arm_mpam: Remove duplicate linux/srcu.h header
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[01-12 16:58]** [PATCH v3 02/47] arm_mpam: Use non-atomic bitops when modifying feature bitmap
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[01-12 16:58]** [PATCH v3 03/47] arm64/sysreg: Add MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[01-12 16:58]** [PATCH v3 04/47] KVM: arm64: Preserve host MPAM configuration when changing traps
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[01-12 16:58]** [PATCH v3 05/47] KVM: arm64: Make MPAMSM_EL1 accesses UNDEF
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[01-12 16:58]** [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
8. **[01-12 16:58]** [PATCH v3 07/47] arm64: mpam: Re-initialise MPAM regs when CPU comes online
   - 发件人: Ben Horgan <ben.horgan@arm.com>
9. **[01-12 16:58]** [PATCH v3 08/47] arm64: mpam: Advertise the CPUs MPAM limits to the driver
   - 发件人: Ben Horgan <ben.horgan@arm.com>
10. **[01-12 16:58]** [PATCH v3 09/47] arm64: mpam: Add cpu_pm notifier to restore MPAM sysregs
   - 发件人: Ben Horgan <ben.horgan@arm.com>
11. **[01-12 16:58]** [PATCH v3 10/47] arm64: mpam: Initialise and context switch the MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
12. **[01-12 16:58]** [PATCH v3 11/47] arm64: mpam: Add helpers to change a task or cpu's MPAM PARTID/PMG values
   - 发件人: Ben Horgan <ben.horgan@arm.com>
13. **[01-12 16:58]** [PATCH v3 12/47] KVM: arm64: Force guest EL1 to use user-space's partid configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
14. **[01-12 16:58]** [PATCH v3 13/47] KVM: arm64: Use kernel-space partid configuration for hypercalls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[01-12 16:58]** [PATCH v3 14/47] arm_mpam: resctrl: Add boilerplate cpuhp and domain allocation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
16. **[01-12 16:58]** [PATCH v3 15/47] arm_mpam: resctrl: Sort the order of the domain lists
   - 发件人: Ben Horgan <ben.horgan@arm.com>
17. **[01-12 16:58]** [PATCH v3 16/47] arm_mpam: resctrl: Pick the caches we will use as resctrl resources
   - 发件人: Ben Horgan <ben.horgan@arm.com>
18. **[01-12 16:58]** [PATCH v3 17/47] arm_mpam: resctrl: Implement resctrl_arch_reset_all_ctrls()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
19. **[01-12 16:58]** [PATCH v3 18/47] arm_mpam: resctrl: Add resctrl_arch_get_config()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
20. **[01-12 16:58]** [PATCH v3 19/47] arm_mpam: resctrl: Implement helpers to update configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
21. **[01-12 16:58]** [PATCH v3 20/47] arm_mpam: resctrl: Add plumbing against arm64 task and cpu hooks
   - 发件人: Ben Horgan <ben.horgan@arm.com>
22. **[01-12 16:58]** [PATCH v3 21/47] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
23. **[01-12 16:58]** [PATCH v3 22/47] arm_mpam: resctrl: Convert to/from MPAMs fixed-point formats
   - 发件人: Ben Horgan <ben.horgan@arm.com>
24. **[01-12 16:58]** [PATCH v3 23/47] arm_mpam: resctrl: Add kunit test for control format conversions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
25. **[01-12 16:58]** [PATCH v3 24/47] arm_mpam: resctrl: Add rmid index helpers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
26. **[01-12 16:58]** [PATCH v3 25/47] arm_mpam: resctrl: Add kunit test for rmid idx conversions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
27. **[01-12 16:58]** [PATCH v3 26/47] arm_mpam: resctrl: Wait for cacheinfo to be ready
   - 发件人: Ben Horgan <ben.horgan@arm.com>
28. **[01-12 16:58]** [PATCH v3 27/47] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
29. **[01-12 16:58]** [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
30. **[01-12 16:58]** [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
31. **[01-12 16:58]** [PATCH v3 30/47] arm_mpam: resctrl: Pre-allocate free running monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
32. **[01-12 16:58]** [PATCH v3 31/47] arm_mpam: resctrl: Pre-allocate assignable monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
33. **[01-12 16:58]** [PATCH v3 32/47] arm_mpam: resctrl: Add kunit test for ABMC/CDP interactions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
34. **[01-12 16:59]** [PATCH v3 33/47] arm_mpam: resctrl: Add resctrl_arch_config_cntr() for ABMC use
   - 发件人: Ben Horgan <ben.horgan@arm.com>
35. **[01-12 16:59]** [PATCH v3 34/47] arm_mpam: resctrl: Allow resctrl to allocate monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
36. **[01-12 16:59]** [PATCH v3 35/47] arm_mpam: resctrl: Add resctrl_arch_rmid_read() and resctrl_arch_reset_rmid()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
37. **[01-12 16:59]** [PATCH v3 36/47] arm_mpam: resctrl: Add resctrl_arch_cntr_read() & resctrl_arch_reset_cntr()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
38. **[01-12 16:59]** [PATCH v3 37/47] arm_mpam: resctrl: Update the rmid reallocation limit
   - 发件人: Ben Horgan <ben.horgan@arm.com>
39. **[01-12 16:59]** [PATCH v3 38/47] arm_mpam: resctrl: Add empty definitions for assorted resctrl functions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
40. **[01-12 16:59]** [PATCH v3 39/47] arm64: mpam: Select ARCH_HAS_CPU_RESCTRL
   - 发件人: Ben Horgan <ben.horgan@arm.com>
41. **[01-12 16:59]** [PATCH v3 40/47] arm_mpam: resctrl: Call resctrl_init() on platforms that can support resctrl
   - 发件人: Ben Horgan <ben.horgan@arm.com>
42. **[01-12 16:59]** [PATCH v3 41/47] arm_mpam: Generate a configuration for min controls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
43. **[01-12 16:59]** [PATCH v3 42/47] arm_mpam: resctrl: Add kunit test for mbw min control generation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
44. **[01-12 16:59]** [PATCH v3 43/47] arm_mpam: Add quirk framework
   - 发件人: Ben Horgan <ben.horgan@arm.com>
45. **[01-12 16:59]** [PATCH v3 44/47] arm_mpam: Add workaround for T241-MPAM-1
   - 发件人: Ben Horgan <ben.horgan@arm.com>
46. **[01-12 16:59]** [PATCH v3 45/47] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
47. **[01-12 16:59]** [PATCH v3 46/47] arm_mpam: Add workaround for T241-MPAM-6
   - 发件人: Ben Horgan <ben.horgan@arm.com>
48. **[01-12 16:59]** [PATCH v3 47/47] arm_mpam: Quirk CMN-650's CSU NRDY behaviour
   - 发件人: Ben Horgan <ben.horgan@arm.com>
49. **[01-12 09:13]** Re: [PATCH v3 01/47] arm_mpam: Remove duplicate linux/srcu.h header
   - 发件人: Fenghua Yu <fenghuay@nvidia.com>
50. **[01-13 14:19]** Re: [PATCH v3 12/47] KVM: arm64: Force guest EL1 to use
 user-space's partid configuration
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
51. **[01-13 14:21]** Re: [PATCH v3 13/47] KVM: arm64: Use kernel-space partid
 configuration for hypercalls
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
52. **[01-13 14:35]** Re: [PATCH v3 13/47] KVM: arm64: Use kernel-space partid
 configuration for hypercalls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
53. **[01-13 14:46]** Re: [PATCH v3 17/47] arm_mpam: resctrl: Implement
 resctrl_arch_reset_all_ctrls()
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
54. **[01-13 14:55]** Re: [PATCH v3 24/47] arm_mpam: resctrl: Add rmid index helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
55. **[01-13 14:58]** Re: [PATCH v3 17/47] arm_mpam: resctrl: Implement
 resctrl_arch_reset_all_ctrls()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
56. **[01-13 14:59]** Re: [PATCH v3 25/47] arm_mpam: resctrl: Add kunit test for rmid idx
 conversions
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
57. **[01-13 15:01]** Re: [PATCH v3 26/47] arm_mpam: resctrl: Wait for cacheinfo to be
 ready
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
58. **[01-13 15:06]** Re: [PATCH v3 27/47] arm_mpam: resctrl: Add support for 'MB'
 resource
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
59. **[01-13 15:10]** Re: [PATCH v3 30/47] arm_mpam: resctrl: Pre-allocate free running
 monitors
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
60. **[01-13 15:15]** Re: [PATCH v3 26/47] arm_mpam: resctrl: Wait for cacheinfo to be
 ready
   - 发件人: Ben Horgan <ben.horgan@arm.com>
61. **[01-13 15:26]** Re: [PATCH v3 32/47] arm_mpam: resctrl: Add kunit test for ABMC/CDP
 interactions
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
62. **[01-13 15:39]** Re: [PATCH v3 41/47] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
63. **[01-13 15:43]** Re: [PATCH v3 42/47] arm_mpam: resctrl: Add kunit test for mbw min
 control generation
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
64. **[01-13 08:49]** Re: [PATCH v3 14/47] arm_mpam: resctrl: Add boilerplate cpuhp and
 domain allocation
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
65. **[01-13 14:18]** Re: [PATCH v3 27/47] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
66. **[01-13 15:14]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
67. **[01-14 14:51]** Re: [PATCH RESEND v2 0/45] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Zeng Heng <zengheng4@huawei.com>
68. **[01-14 12:06]** Re: [PATCH v3 12/47] KVM: arm64: Force guest EL1 to use user-space's partid configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
69. **[01-14 12:09]** Re: [PATCH v3 13/47] KVM: arm64: Use kernel-space partid configuration for hypercalls
   - 发件人: Marc Zyngier <maz@kernel.org>
70. **[01-14 14:39]** Re: [PATCH v3 13/47] KVM: arm64: Use kernel-space partid
 configuration for hypercalls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
71. **[01-14 14:50]** Re: [PATCH v3 12/47] KVM: arm64: Force guest EL1 to use user-space's
 partid configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
72. **[01-14 16:50]** Re: [PATCH v3 13/47] KVM: arm64: Use kernel-space partid
 configuration for hypercalls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
73. **[01-14 17:50]** Re: [PATCH v3 13/47] KVM: arm64: Use kernel-space partid configuration for hypercalls
   - 发件人: Marc Zyngier <maz@kernel.org>
74. **[01-15 10:12]** Re: [PATCH v3 01/47] arm_mpam: Remove duplicate linux/srcu.h header
   - 发件人: Gavin Shan <gshan@redhat.com>
75. **[01-15 10:14]** Re: [PATCH v3 02/47] arm_mpam: Use non-atomic bitops when modifying
 feature bitmap
   - 发件人: Gavin Shan <gshan@redhat.com>
76. **[01-15 10:16]** Re: [PATCH v3 03/47] arm64/sysreg: Add MPAMSM_EL1 register
   - 发件人: Gavin Shan <gshan@redhat.com>
77. **[01-15 10:33]** Re: [PATCH v3 04/47] KVM: arm64: Preserve host MPAM configuration
 when changing traps
   - 发件人: Gavin Shan <gshan@redhat.com>
78. **[01-15 10:34]** Re: [PATCH v3 05/47] KVM: arm64: Make MPAMSM_EL1 accesses UNDEF
   - 发件人: Gavin Shan <gshan@redhat.com>
79. **[01-15 14:47]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Gavin Shan <gshan@redhat.com>
80. **[01-15 14:50]** Re: [PATCH v3 07/47] arm64: mpam: Re-initialise MPAM regs when CPU
 comes online
   - 发件人: Gavin Shan <gshan@redhat.com>
81. **[01-15 09:05]** Re: [PATCH v3 12/47] KVM: arm64: Force guest EL1 to use user-space's partid configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
82. **[01-15 10:05]** Re: [PATCH v3 37/47] arm_mpam: resctrl: Update the rmid reallocation
 limit
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
83. **[01-15 12:14]** Re: [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Peter Newman <peternewman@google.com>
84. **[01-15 11:14]** Re: [PATCH v3 12/47] KVM: arm64: Force guest EL1 to use user-space's
 partid configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
85. **[01-15 11:36]** Re: [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
86. **[01-15 12:09]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
87. **[01-15 14:37]** Re: [PATCH RESEND v2 0/45] arm_mpam: Add KVM/arm64 and resctrl glue
 code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
88. **[01-15 15:43]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
89. **[01-15 16:49]** Re: [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Peter Newman <peternewman@google.com>
90. **[01-15 16:02]** Re: [PATCH v3 37/47] arm_mpam: resctrl: Update the rmid reallocation
 limit
   - 发件人: Ben Horgan <ben.horgan@arm.com>
91. **[01-15 17:58]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
92. **[01-15 17:59]** Re: [PATCH v3 03/47] arm64/sysreg: Add MPAMSM_EL1 register
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
93. **[01-15 18:14]** Re: [PATCH v3 07/47] arm64: mpam: Re-initialise MPAM regs when CPU
 comes online
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
94. **[01-15 18:16]** Re: [PATCH v3 08/47] arm64: mpam: Advertise the CPUs MPAM limits to
 the driver
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
95. **[01-15 18:20]** Re: [PATCH v3 09/47] arm64: mpam: Add cpu_pm notifier to restore
 MPAM sysregs
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
96. **[01-15 10:54]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
97. **[01-15 19:08]** Re: [PATCH v3 10/47] arm64: mpam: Initialise and context switch the
 MPAMSM_EL1 register
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
98. **[01-15 19:13]** Re: [PATCH v3 11/47] arm64: mpam: Add helpers to change a task or
 cpu's MPAM PARTID/PMG values
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
99. **[01-15 19:16]** Re: [PATCH v3 39/47] arm64: mpam: Select ARCH_HAS_CPU_RESCTRL
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
100. **[01-15 15:20]** Re: [PATCH v3 45/47] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Fenghua Yu <fenghuay@nvidia.com>
101. **[01-16 10:29]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
102. **[01-16 10:34]** Re: [PATCH v3 31/47] arm_mpam: resctrl: Pre-allocate assignable
 monitors
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
103. **[01-16 10:47]** Re: [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
104. **[01-16 11:04]** Re: [PATCH v3 31/47] arm_mpam: resctrl: Pre-allocate assignable
 monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
105. **[01-16 11:05]** Re: [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
106. **[01-16 11:57]** Re: [PATCH v3 02/47] arm_mpam: Use non-atomic bitops when modifying
 feature bitmap
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
107. **[01-16 12:02]** Re: [PATCH v3 02/47] arm_mpam: Use non-atomic bitops when modifying
 feature bitmap
   - 发件人: Ben Horgan <ben.horgan@arm.com>
108. **[01-16 12:12]** Re: [PATCH v3 02/47] arm_mpam: Use non-atomic bitops when modifying
 feature bitmap
   - 发件人: Ben Horgan <ben.horgan@arm.com>
109. **[01-16 15:47]** Re: (subset) [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl
 glue code
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
110. **[01-16 15:51]** Re: [PATCH v3 02/47] arm_mpam: Use non-atomic bitops when modifying
 feature bitmap
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 2: [PATCH v9 00/13] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 48 | **👥 参与者**: 10 | **📅 开始时间**: Wed, 14 Jan 2026 13:45:12 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主题为“支持从直接映射中移除 guest_memfd”。该补丁旨在通过从主机内核的直接映射中解除虚拟机客户内存的映射，以缓解 Spectre 风格的瞬态执行问题。

**原始补丁/问题内容**：
补丁系列的核心是扩展 guest_memfd，使其能够在 KVM 客户中移除内存的直接映射，从而提高安全性。补丁中引入了多个新功能，包括 folio_{zap,restore}_direct_map 辅助函数，以及 GUEST_MEMFD_FLAG_NO_DIRECT_MAP 标志。

**之前讨论要点**：
在历史讨论中，参与者们讨论了补丁的设计和实现细节，包括如何处理直接映射的清除和恢复，以及不同架构（如 x86 和 arm64）对这些操作的支持。补丁的设计没有发生实质性变化，但根据反馈进行了多次调整和优化。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现和测试上。参与者们提出了对补丁的改进建议，例如简化代码、优化性能，以及确保新功能在不同虚拟机环境中的兼容性。特别是，讨论了如何处理 TDX 虚拟机的特殊情况，确保安全性和性能之间的平衡。此外，补丁系列的自测试也得到了扩展，以验证新功能的有效性。整体来看，补丁系列在功能和安全性方面的实现得到了认可，后续将继续优化性能。

#### 📝 邮件列表

1. **[01-14 13:45]** [PATCH v9 00/13] Direct Map Removal Support for guest_memfd
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
2. **[01-14 13:45]** [PATCH v9 01/13] set_memory: add folio_{zap,restore}_direct_map
 helpers
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
3. **[01-14 13:45]** [PATCH v9 02/13] mm/gup: drop secretmem optimization from
 gup_fast_folio_allowed
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
4. **[01-14 13:45]** [PATCH v9 03/13] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
5. **[01-14 13:45]** [PATCH v9 04/13] KVM: guest_memfd: Add stub for
 kvm_arch_gmem_invalidate
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
6. **[01-14 13:46]** [PATCH v9 05/13] KVM: x86: define
 kvm_arch_gmem_supports_no_direct_map()
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
7. **[01-14 13:46]** [PATCH v9 06/13] KVM: arm64: define
 kvm_arch_gmem_supports_no_direct_map()
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
8. **[01-14 13:46]** [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
9. **[01-14 13:46]** [PATCH v9 08/13] KVM: selftests: load elf via bounce buffer
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
10. **[01-14 13:46]** [PATCH v9 09/13] KVM: selftests: set KVM_MEM_GUEST_MEMFD in
 vm_mem_add() if guest_memfd != -1
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
11. **[01-14 13:47]** [PATCH v9 10/13] KVM: selftests: Add guest_memfd based
 vm_mem_backing_src_types
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
12. **[01-14 13:47]** [PATCH v9 11/13] KVM: selftests: cover GUEST_MEMFD_FLAG_NO_DIRECT_MAP
 in existing selftests
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
13. **[01-14 13:47]** [PATCH v9 12/13] KVM: selftests: stuff vm_mem_backing_src_type into
 vm_shape
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
14. **[01-14 13:47]** [PATCH v9 13/13] KVM: selftests: Test guest execution from direct map
 removed gmem
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
15. **[01-15 18:54]** Re: [PATCH v9 01/13] set_memory: add folio_{zap,restore}_direct_map helpers
   - 发件人: Huacai Chen <chenhuacai@kernel.org>
16. **[01-15 11:03]** Re: [PATCH v9 01/13] set_memory: add folio_{zap, restore}_direct_map
 helpers
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
17. **[01-15 13:12]** Re: [PATCH v9 01/13] set_memory: add folio_{zap,restore}_direct_map
 helpers
   - 发件人: Heiko Carstens <hca@linux.ibm.com>
18. **[01-15 15:25]** Re: [PATCH v9 01/13] set_memory: add folio_{zap, restore}_direct_map
 helpers
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
19. **[01-15 15:55]** Re: [PATCH v9 01/13] set_memory: add folio_{zap,restore}_direct_map
 helpers
   - 发件人: Matthew Wilcox <willy@infradead.org>
20. **[01-15 17:45]** Re: [PATCH v9 01/13] set_memory: add folio_{zap, restore}_direct_map
 helpers
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
21. **[01-15 11:39]** Re: [PATCH v9 09/13] KVM: selftests: set KVM_MEM_GUEST_MEMFD in
 vm_mem_add() if guest_memfd != -1
   - 发件人: Ackerley Tng <ackerleytng@google.com>
22. **[01-15 12:00]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
23. **[01-15 21:04]** Re: [PATCH v9 02/13] mm/gup: drop secretmem optimization from
 gup_fast_folio_allowed
   - 发件人: David Hildenbrand (Red Hat) <david@kernel.org>
24. **[01-15 21:05]** Re: [PATCH v9 01/13] set_memory: add folio_{zap, restore}_direct_map
 helpers
   - 发件人: David Hildenbrand (Red Hat) <david@kernel.org>
25. **[01-15 13:07]** Re: [PATCH v9 01/13] set_memory: add folio_{zap,restore}_direct_map helpers
   - 发件人: Ackerley Tng <ackerleytng@google.com>
26. **[01-15 13:40]** Re: [PATCH v9 02/13] mm/gup: drop secretmem optimization from gup_fast_folio_allowed
   - 发件人: Ackerley Tng <ackerleytng@google.com>
27. **[01-15 13:42]** Re: [PATCH v9 03/13] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Ackerley Tng <ackerleytng@google.com>
28. **[01-15 13:47]** Re: [PATCH v9 04/13] KVM: guest_memfd: Add stub for kvm_arch_gmem_invalidate
   - 发件人: Ackerley Tng <ackerleytng@google.com>
29. **[01-15 13:48]** Re: [PATCH v9 05/13] KVM: x86: define kvm_arch_gmem_supports_no_direct_map()
   - 发件人: Ackerley Tng <ackerleytng@google.com>
30. **[01-15 23:04]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
31. **[01-16 00:00]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
32. **[01-16 14:55]** Re: [PATCH v9 02/13] mm/gup: drop secretmem optimization from
 gup_fast_folio_allowed
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
33. **[01-16 14:56]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
34. **[01-16 15:00]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
35. **[01-16 15:00]** Re: [PATCH v9 09/13] KVM: selftests: set KVM_MEM_GUEST_MEMFD in
 vm_mem_add() if guest_memfd != -1
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
36. **[01-16 15:02]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
37. **[01-16 15:34]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
38. **[01-16 15:35]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
39. **[01-16 07:41]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Sean Christopherson <seanjc@google.com>
40. **[01-16 17:28]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
41. **[01-16 09:30]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Vishal Annapurve <vannapurve@google.com>
42. **[01-16 17:32]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
43. **[01-16 17:36]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
44. **[01-16 17:51]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
45. **[01-16 17:51]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
46. **[01-16 17:51]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
47. **[01-16 18:10]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
48. **[01-16 18:16]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>

---

### Thread 3: [PATCH v3 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support

**📧 邮件数**: 43 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 9 Jan 2026 17:04:39 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下引入虚拟 GICv5（vgic_v5）及其对 PPI（Private Peripheral Interrupt）支持的补丁系列。该补丁系列的主要目标是实现对 GICv5 的支持，初步版本仅实现了 PPI 的功能，后续将继续扩展支持 SPI（Shared Peripheral Interrupt）、LPI（Low-Priority Interrupt）等。

在历史讨论中，Sascha Bischoff 提出了多个补丁，涵盖了 GICv5 的初始化、寄存器处理、PPIs 的管理等方面。主要讨论要点包括如何在 KVM 中正确处理 GICv5 的中断类型、寄存器映射以及如何确保虚拟机的状态与物理硬件一致。

在本周的新讨论中，参与者 Jonathan Cameron 对多个补丁进行了审查，给予了“Reviewed-by”的反馈，表明这些补丁在技术上是可接受的。讨论中还提出了一些小的改进建议，例如对代码的清晰度和可读性进行优化。此外，Joey Gouly 提出了对 PPI 状态同步机制的疑问，建议更新提交信息以解释相关逻辑。

总体来看，本周的讨论主要集中在对补丁的审查和小幅改进建议上，显示出社区对 GICv5 支持的积极关注和合作。

#### 📝 邮件列表

1. **[01-09 17:04]** [PATCH v3 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[01-09 17:04]** [PATCH v3 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use generated
 ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[01-09 17:04]** [PATCH v3 03/36] arm64/sysreg: Drop ICH_HFGRTR_EL2.ICC_HAPR_EL1 and
 make RES1
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[01-09 17:04]** [PATCH v3 06/36] KVM: arm64: gic: Set vgic_model before initing
 private IRQs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[01-09 17:04]** [PATCH v3 05/36] arm64/sysreg: Add GICR CDNMIA encoding
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[01-09 17:04]** [PATCH v3 08/36] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[01-09 17:04]** [PATCH v3 09/36] KVM: arm64: gic-v5: Add Arm copyright header
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[01-09 17:04]** [PATCH v3 07/36] KVM: arm64: gic-v5: Add ARM_VGIC_V5 device to KVM
 headers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
9. **[01-09 17:04]** [PATCH v3 12/36] KVM: arm64: gic-v5: Support GICv5 FGTs & FGUs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[01-09 17:04]** [PATCH v3 10/36] KVM: arm64: gic-v5: Detect implemented PPIs on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
11. **[01-09 17:04]** [PATCH v3 11/36] KVM: arm64: gic-v5: Sanitize ID_AA64PFR2_EL1.GCIE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[01-09 17:04]** [PATCH v3 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[01-09 17:04]** [PATCH v3 19/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[01-09 17:04]** [PATCH v3 22/36] KVM: arm64: gic-v5: Trap and mask guest
 ICC_PPI_ENABLERx_EL1 writes
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[01-09 17:04]** [PATCH v3 21/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
16. **[01-09 17:04]** [PATCH v3 26/36] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[01-09 17:04]** [PATCH v3 27/36] KVM: arm64: gic-v5: Mandate architected PPI for PMU
 emulation on GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
18. **[01-09 17:04]** [PATCH v3 24/36] KVM: arm64: gic-v5: Create, init vgic_v5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
19. **[01-09 17:04]** [PATCH v3 30/36] KVM: arm64: gic-v5: Introduce kvm_arm_vgic_v5_ops
 and register them
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
20. **[01-09 17:04]** [PATCH v3 35/36] KVM: arm64: selftests: Introduce a minimal GICv5 PPI
 selftest
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
21. **[01-09 17:04]** [PATCH v3 36/36] KVM: arm64: gic-v5: Communicate userspace-driveable
 PPIs via a UAPI
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
22. **[01-12 14:00]** Re: [PATCH v3 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
23. **[01-12 14:03]** Re: [PATCH v3 03/36] arm64/sysreg: Drop ICH_HFGRTR_EL2.ICC_HAPR_EL1
 and make RES1
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
24. **[01-12 14:37]** Re: [PATCH v3 06/36] KVM: arm64: gic: Set vgic_model before initing
 private IRQs
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
25. **[01-12 14:39]** Re: [PATCH v3 05/36] arm64/sysreg: Add GICR CDNMIA encoding
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
26. **[01-12 14:41]** Re: [PATCH v3 07/36] KVM: arm64: gic-v5: Add ARM_VGIC_V5 device to
 KVM headers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
27. **[01-12 14:44]** Re: [PATCH v3 08/36] KVM: arm64: gic: Introduce interrupt type
 helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
28. **[01-12 14:45]** Re: [PATCH v3 09/36] KVM: arm64: gic-v5: Add Arm copyright header
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
29. **[01-12 14:47]** Re: [PATCH v3 11/36] KVM: arm64: gic-v5: Sanitize
 ID_AA64PFR2_EL1.GCIE
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
30. **[01-12 14:52]** Re: [PATCH v3 10/36] KVM: arm64: gic-v5: Detect implemented PPIs on
 boot
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
31. **[01-12 14:55]** Re: [PATCH v3 12/36] KVM: arm64: gic-v5: Support GICv5 FGTs & FGUs
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
32. **[01-12 15:49]** Re: [PATCH v3 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put
 and save/restore
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
33. **[01-12 16:01]** Re: [PATCH v3 19/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
34. **[01-12 16:13]** Re: [PATCH v3 21/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
35. **[01-12 16:16]** Re: [PATCH v3 22/36] KVM: arm64: gic-v5: Trap and mask guest
 ICC_PPI_ENABLERx_EL1 writes
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
36. **[01-12 16:20]** Re: [PATCH v3 24/36] KVM: arm64: gic-v5: Create, init vgic_v5
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
37. **[01-12 16:27]** Re: [PATCH v3 26/36] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
38. **[01-12 16:28]** Re: [PATCH v3 27/36] KVM: arm64: gic-v5: Mandate architected PPI
 for PMU emulation on GICv5
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
39. **[01-12 16:29]** Re: [PATCH v3 30/36] KVM: arm64: gic-v5: Introduce
 kvm_arm_vgic_v5_ops and register them
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
40. **[01-12 16:38]** Re: [PATCH v3 35/36] KVM: arm64: selftests: Introduce a minimal
 GICv5 PPI selftest
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
41. **[01-12 16:42]** Re: [PATCH v3 36/36] KVM: arm64: gic-v5: Communicate
 userspace-driveable PPIs via a UAPI
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
42. **[01-13 12:11]** Re: [PATCH v3 27/36] KVM: arm64: gic-v5: Mandate architected PPI for
 PMU emulation on GICv5
   - 发件人: Joey Gouly <joey.gouly@arm.com>
43. **[01-13 12:16]** Re: [PATCH v3 21/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 4: [PATCH v9 00/30] Tracefs support for pKVM

**📧 邮件数**: 27 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 07 Jan 2026 16:00:19 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的第九版补丁（PATCH v9 00/30）。该补丁旨在增强 KVM 的功能，特别是对 SME（Scalable Matrix Extension）寄存器的支持。

在历史讨论中，Marc Zyngier 表达了对补丁的积极看法，并指出需要相关维护者的确认。Steven Rostedt 也表示会尽快完成审查。Fuad Tabba 提出了对某些补丁的命名和功能的细节问题，强调了代码的准确性。

在本周的新讨论中，Fuad Tabba 和 Mark Brown 继续对补丁进行深入审查，讨论了多个补丁的具体实现细节，包括对寄存器访问的汇编实现、状态切换的处理以及对用户空间的暴露等。特别是，Fuad 提出了对某些操作的优化建议，并讨论了在不同向量长度（VL）下的状态管理问题。此外，Mark 也关注到补丁中可能存在的顺序依赖性问题，并建议在文档中进行详细说明。

总体来看，讨论集中在补丁的细节审查和潜在问题的解决上，参与者们积极交流，以确保补丁的质量和功能的正确性。

#### 📝 邮件列表

1. **[01-07 16:00]** Re: [PATCH v9 00/30] Tracefs support for pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-07 11:59]** Re: [PATCH v9 00/30] Tracefs support for pKVM
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
3. **[01-09 15:59]** Re: [PATCH v9 14/30] KVM: arm64: Implement SME vector length configuration
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[01-12 11:59]** Re: [PATCH v9 18/30] KVM: arm64: Support SME priority registers
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[01-12 13:27]** Re: [PATCH v9 14/30] KVM: arm64: Implement SME vector length
 configuration
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[01-12 13:28]** Re: [PATCH v9 14/30] KVM: arm64: Implement SME vector length configuration
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[01-12 17:59]** Re: [PATCH v9 19/30] KVM: arm64: Provide assembly for SME register access
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[01-12 18:35]** Re: [PATCH v9 20/30] KVM: arm64: Support userspace access to
 streaming mode Z and P registers
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[01-12 19:08]** Re: [PATCH v9 21/30] KVM: arm64: Flush register state on writes to
 SVCR.SM and SVCR.ZA
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[01-13 10:05]** Re: [PATCH v9 27/30] KVM: arm64: selftests: Remove spurious check for
 single bit safe values
   - 发件人: Ben Horgan <ben.horgan@arm.com>
11. **[01-13 10:52]** Re: [PATCH v9 28/30] KVM: arm64: selftests: Skip impossible invalid
 value tests
   - 发件人: Ben Horgan <ben.horgan@arm.com>
12. **[01-13 14:06]** Re: [PATCH v9 22/30] KVM: arm64: Expose SME specific state to userspace
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[01-13 14:24]** Re: [PATCH v9 23/30] KVM: arm64: Context switch SME state for guests
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[01-13 14:29]** Re: [PATCH v9 24/30] KVM: arm64: Handle SME exceptions
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[01-13 14:37]** Re: [PATCH v9 25/30] KVM: arm64: Expose SME to nested guests
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[01-13 14:40]** Re: [PATCH v9 26/30] KVM: arm64: Provide interface for configuring
 and enabling SME for guests
   - 发件人: Fuad Tabba <tabba@google.com>
17. **[01-13 14:58]** Re: [PATCH v9 00/30] KVM: arm64: Implement support for SME
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[01-13 16:10]** Re: [PATCH v9 00/30] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
19. **[01-13 19:08]** Re: [PATCH v9 18/30] KVM: arm64: Support SME priority registers
   - 发件人: Mark Brown <broonie@kernel.org>
20. **[01-13 19:20]** Re: [PATCH v9 19/30] KVM: arm64: Provide assembly for SME register
 access
   - 发件人: Mark Brown <broonie@kernel.org>
21. **[01-14 10:08]** Re: [PATCH v9 19/30] KVM: arm64: Provide assembly for SME register access
   - 发件人: Fuad Tabba <tabba@google.com>
22. **[01-14 17:07]** Re: [PATCH v9 22/30] KVM: arm64: Expose SME specific state to
 userspace
   - 发件人: Mark Brown <broonie@kernel.org>
23. **[01-14 17:27]** Re: [PATCH v9 23/30] KVM: arm64: Context switch SME state for guests
   - 发件人: Mark Brown <broonie@kernel.org>
24. **[01-14 18:22]** Re: [PATCH v9 25/30] KVM: arm64: Expose SME to nested guests
   - 发件人: Mark Brown <broonie@kernel.org>
25. **[01-14 18:48]** Re: [PATCH v9 26/30] KVM: arm64: Provide interface for configuring
 and enabling SME for guests
   - 发件人: Mark Brown <broonie@kernel.org>
26. **[01-15 09:02]** Re: [PATCH v9 23/30] KVM: arm64: Context switch SME state for guests
   - 发件人: Fuad Tabba <tabba@google.com>
27. **[01-16 10:08]** Re: [PATCH v9 00/30] Tracefs support for pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 5: [PATCH kvmtool v2 00/17] arm64: Support GICv5-based guests

**📧 邮件数**: 18 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 16 Jan 2026 18:26:06 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM 工具的补丁系列，主要是为了支持 GICv5（通用中断控制器版本5）虚拟机的功能。

1. **原始补丁/问题内容**：该补丁系列（共17个补丁）旨在为 KVM 工具添加对 GICv5 的支持，具体包括对 PPIs（私有中断）、IRS（中断路由服务）和 ITS（中断翻译服务）的支持。补丁的基础是之前的嵌套虚拟化系列，并且在此基础上进行了更新。

2. **之前讨论要点**：在历史讨论中，补丁的早期版本（v1）被意外地基于旧版本，导致了一些问题。此次更新（v2）修复了这些问题，并进行了代码清理和功能增强。

3. **本周的新讨论、进展或结论**：本周的讨论集中在多个补丁的提交上，包括：
   - 添加了基本的 GICv5 支持，能够创建虚拟机并使用 PPIs。
   - 引入了 GICv5 特有的 FDT（设备树）节点生成函数。
   - 更新了 PMU（性能监控单元）和定时器的中断描述符以支持 GICv5。
   - 增加了对 GICv5 ITS 的支持，使得虚拟机能够使用 MSIs（消息中断）。
   - 讨论了如何在 FDT 中正确描述 GICv5 的中断，并确保与现有系统的兼容性。

整体来看，这些补丁的实施将极大地增强 KVM 在 ARM64 架构上的功能，特别是在处理 GICv5 相关的中断时。

#### 📝 邮件列表

1. **[01-16 18:26]** [PATCH kvmtool v2 00/17] arm64: Support GICv5-based guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[01-16 18:26]** [PATCH kvmtool v2 01/17] Sync kernel UAPI headers with v6.19-rc5 with
 WIP KVM GICv5 PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[01-16 18:26]** [PATCH kvmtool v2 02/17] arm64: Add basic support for creating a VM
 with GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[01-16 18:26]** [PATCH kvmtool v2 03/17] arm64: Simplify GICv5 type checks by adding
 gic__is_v5()
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[01-16 18:26]** [PATCH kvmtool v2 04/17] arm64: Introduce GICv5 FDT IRQ types
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[01-16 18:26]** [PATCH kvmtool v2 05/17] arm64: Generate GICv5 FDT node
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[01-16 18:26]** [PATCH kvmtool v2 06/17] arm64: Update PMU IRQ and FDT code for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[01-16 18:26]** [PATCH kvmtool v2 07/17] arm64: Update timer FDT IRQsfor GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
9. **[01-16 18:26]** [PATCH kvmtool v2 08/17] irq: Add interface to override default irq
 offset
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[01-16 18:26]** [PATCH kvmtool v2 09/17] arm64: Add phandle for each CPU
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
11. **[01-16 18:27]** [PATCH kvmtool v2 10/17] Sync kernel headers with v6.19-rc5 for GICv5
 IRS and ITS support in KVM
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[01-16 18:27]** [PATCH kvmtool v2 11/17] arm64: Add GICv5 IRS support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[01-16 18:27]** [PATCH kvmtool v2 12/17] arm64: Generate FDT node for GICv5's IRS
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[01-16 18:27]** [PATCH kvmtool v2 13/17] arm64: Update generic FDT interrupt desc
 generator for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[01-16 18:27]** [PATCH kvmtool v2 14/17] arm64: Bump PCI FDT code for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
16. **[01-16 18:27]** [PATCH kvmtool v2 15/17] arm64: Introduce gicv5-its irqchip
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[01-16 18:27]** [PATCH kvmtool v2 16/17] arm64: Add GICv5 ITS node to FDT
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
18. **[01-16 18:27]** [PATCH kvmtool v2 17/17] arm64: Update PCI FDT generation for GICv5
 ITS MSIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 6: [PATCH 00/30] KVM: arm64: Add support for protected guest memory with pKVM

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Mon,  5 Jan 2026 15:49:08 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是为 KVM（Kernel-based Virtual Machine）在 arm64 架构上添加对受保护来宾内存（protected guest memory）支持的补丁系列（PATCH 00/30）。该补丁旨在解决 pKVM 在上游支持不足的问题，尤其是在用户空间如何暴露受保护虚拟机（pVM）方面的挑战。

在历史讨论中，Will Deacon 提出了多个补丁，主要包括对页表的所有者信息进行通用化处理，以及在主机的二级页表中标注来宾内存捐赠的句柄和来宾页框号（gfn）。讨论中，参与者们提出了对注释类型的建议，认为可以在注释中直接包含类型信息，以提高代码的可读性和健壮性。

在本周的新讨论中，Fuad Tabba 对之前的补丁表示认可，并确认了一些细节。Will Deacon 也更新了补丁，增加了类型和注释的处理，但指出在编码来宾 gfn 和句柄时面临位数不足的问题。他提到，尽管存在复杂性，但这一改进是有益的，并计划在下一个版本中进一步调整。

总体来看，本周的讨论主要集中在补丁的细节调整和对未来可能的改进方向的探讨。

#### 📝 邮件列表

1. **[01-05 15:49]** [PATCH 00/30] KVM: arm64: Add support for protected guest memory with pKVM
   - 发件人: Will Deacon <will@kernel.org>
2. **[01-05 15:49]** [PATCH 17/30] KVM: arm64: Generalise kvm_pgtable_stage2_set_owner()
   - 发件人: Will Deacon <will@kernel.org>
3. **[01-05 15:49]** [PATCH 19/30] KVM: arm64: Annotate guest donations with handle and gfn in host stage-2
   - 发件人: Will Deacon <will@kernel.org>
4. **[01-06 15:20]** Re: [PATCH 17/30] KVM: arm64: Generalise
 kvm_pgtable_stage2_set_owner()
   - 发件人: Quentin Perret <qperret@google.com>
5. **[01-06 16:01]** Re: [PATCH 19/30] KVM: arm64: Annotate guest donations with handle
 and gfn in host stage-2
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[01-09 14:42]** Re: [PATCH 19/30] KVM: arm64: Annotate guest donations with handle
 and gfn in host stage-2
   - 发件人: Will Deacon <will@kernel.org>
7. **[01-09 18:46]** Re: [PATCH 17/30] KVM: arm64: Generalise
 kvm_pgtable_stage2_set_owner()
   - 发件人: Will Deacon <will@kernel.org>
8. **[01-12 09:25]** Re: [PATCH 19/30] KVM: arm64: Annotate guest donations with handle
 and gfn in host stage-2
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[01-17 00:03]** Re: [PATCH 17/30] KVM: arm64: Generalise
 kvm_pgtable_stage2_set_owner()
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 7: [PATCH v4 0/3] KVM ARM64 pre_fault_memory

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 13 Jan 2026 15:26:39 +0000

#### 🤖 AI 总结

本邮件线程讨论了 Jack Thomson 提出的补丁系列 [PATCH v4 0/3]，旨在为 KVM ARM64 添加对 KVM_PRE_FAULT_MEMORY 功能的支持。该功能之前仅在 x86 上可用，能够减少执行过程中的 stage-2 故障，尤其在内存密集型应用的后复制迁移场景中具有显著的延迟改善。

在历史讨论中，补丁的主要内容包括：
1. 第一个补丁实现了 ARM64 上的 KVM_PRE_FAULT_MEMORY ioctl 支持。
2. 第二个补丁更新了 pre_fault_memory_test 以支持 ARM64。
3. 最后一个补丁扩展了测试以涵盖不同的虚拟机内存后备。

本周的讨论中，Jack 针对补丁的实现细节进行了进一步的阐述，并回应了之前的审查意见，特别是关于如何处理嵌套虚拟机的 fault 逻辑。Marc Zyngier 提出了对补丁的批评，认为当前的实现存在问题，特别是在处理嵌套上下文时的错误处理和用户空间的交互问题。Jack 认可了这些意见，并表示将进行相应的修改，以确保补丁在支持预故障的同时，能够妥善处理嵌套虚拟机的情况。

整体来看，讨论集中在补丁的实现细节、潜在问题及其解决方案上，参与者们积极交流，推动了补丁的改进。

#### 📝 邮件列表

1. **[01-13 15:26]** [PATCH v4 0/3] KVM ARM64 pre_fault_memory
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
2. **[01-13 15:26]** [PATCH v4 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
3. **[01-13 15:26]** [PATCH v4 2/3] KVM: selftests: Enable pre_fault_memory_test for arm64
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
4. **[01-13 15:26]** [PATCH v4 3/3] KVM: selftests: Add option for different backing in pre-fault tests
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
5. **[01-15 09:51]** Re: [PATCH v4 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[01-16 14:33]** Re: [PATCH v4 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>
7. **[01-18 10:29]** Re: [PATCH v4 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v6 8/9] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 15 Jan 2026 15:03:43 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要关注如何检查 VM IOCTL（输入输出控制）在 pKVM（保护 KVM）中的有效性。

原始补丁（PATCH v6 8/9）旨在确保在 pKVM 环境中，只有被允许的 VM IOCTL 才能被执行。补丁的背景是为了增强 KVM 的安全性和稳定性，避免潜在的内部问题影响用户空间。

在之前的讨论中，Marc Zyngier 和 Fuad Tabba 讨论了是否可以依赖现有的 VM 能力（KVM_CAP_ARM_BASIC），而不是引入新的用户空间暴露。Marc 提出可以将其定义为 KVM_CAP_NR_VCPUS 的别名，以简化实现。

本周的新讨论中，Fuad 表示他已对补丁进行了修改，并建议将别名定义放在 `asm/kvm_pkvm.h` 中，以便于在补丁中正确引用。Marc 认可这一修改，并表示感谢。最终，Fuad 确认将会合并这些更改，并感谢 Marc 的修复。

总体而言，本周的讨论集中在补丁的具体实现细节上，双方达成了一致意见，确保补丁能够顺利推进。

#### 📝 邮件列表

1. **[01-15 15:03]** Re: [PATCH v6 8/9] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-15 15:19]** Re: [PATCH v6 8/9] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[01-15 16:05]** Re: [PATCH v6 8/9] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[01-15 16:14]** Re: [PATCH v6 8/9] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[01-15 18:03]** Re: [PATCH v6 8/9] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[01-15 19:15]** Re: [PATCH v6 8/9] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[01-15 21:55]** Re: [PATCH v6 0/9] KVM: arm64: Fixes for guest CPU feature trapping and enabling
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 9: [PATCH v2 18/45] arm_mpam: resctrl: Implement
 resctrl_arch_reset_all_ctrls()

**📧 邮件数**: 5 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 5 Jan 2026 17:51:54 +0000

#### 🤖 AI 总结

在本邮件讨论中，主题为“[PATCH v2 18/45] arm_mpam: resctrl: 实现 resctrl_arch_reset_all_ctrls()”。该补丁旨在实现一个函数，用于重置与资源控制相关的所有控制器。

**历史讨论**中，参与者对补丁的必要性提出了质疑。Ben Horgan 指出，mpam_reset_class() 的暴露似乎没有必要，因为只有其锁定版本在外部使用。Zeng Heng 也提到，mpam_cpu_offline() 已经直接调用了 mpam_reset_ris() 来重置即将下线的 MPAM MSC，因此不明白为何还需要在此补丁中调用 mpam_resctrl_offline_cpu()。

**本周的新讨论**中，Ben Horgan 对 Zeng Heng 的疑问做出了回应，承认当前的实现可能存在问题。他表示，组件通常与多个 CPU 相关联，因此在最后一个 CPU 下线时才应进行组件级重置。他承诺将重新审视 CPU 的上下线代码，以确保逻辑的正确性。

总体而言，讨论围绕补丁的必要性和实现细节展开，参与者们对当前实现提出了改进建议，期待进一步的审查和修正。

#### 📝 邮件列表

1. **[01-05 17:51]** Re: [PATCH v2 18/45] arm_mpam: resctrl: Implement
 resctrl_arch_reset_all_ctrls()
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
2. **[01-08 10:42]** Re: [PATCH v2 25/45] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
3. **[01-09 11:45]** Re: [PATCH v2 18/45] arm_mpam: resctrl: Implement resctrl_arch_reset_all_ctrls()
   - 发件人: Zeng Heng <zengheng4@huawei.com>
4. **[01-12 16:45]** Re: [PATCH v2 25/45] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[01-13 17:18]** Re: [PATCH v2 18/45] arm_mpam: resctrl: Implement
 resctrl_arch_reset_all_ctrls()
   - 发件人: Ben Horgan <ben.horgan@arm.com>

---

### Thread 10: [PATCH v8 05/13] KVM: guest_memfd: Add flag to remove from direct
 map

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 14 Jan 2026 13:55:43 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于一个补丁（PATCH v8 05/13），其内容是为 KVM（内核虚拟机）中的 guest_memfd 添加一个标志，以便从直接映射中移除。这个补丁旨在优化内存管理，提升虚拟化性能。

在之前的讨论中，参与者们主要集中在补丁的实现细节和潜在问题上。Vlastimil Babka 和 Dave Hansen 等人对补丁的修改提出了建议，并确认了一些问题的修复，表示在后续版本（v9）中进行了相应的调整。

在本周的新讨论中，Nikita Kalyazin 汇总了之前的反馈，并确认已经在 v9 版本中解决了提到的问题，包括对补丁的拆分和其他细节的完善。整体来看，本周的讨论主要是对补丁的进一步优化和确认，没有出现新的争议或问题，显示出参与者们对补丁的认可和支持。

#### 📝 邮件列表

1. **[01-14 13:55]** Re: [PATCH v8 05/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
2. **[01-14 13:56]** Re: [PATCH v8 05/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
3. **[01-14 13:56]** Re: [PATCH v8 03/13] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
4. **[01-14 13:57]** Re: [PATCH v8 01/13] x86: export set_direct_map_valid_noflush to KVM
 module
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>

---

### Thread 11: [PATCH v2 0/1] KVM: arm64: Calculate hyp VA size only once

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 13 Jan 2026 19:44:08 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的一个补丁，旨在确保虚拟地址（VA）大小的计算只进行一次，以保持内存布局和 MMU 初始化逻辑的一致性。

**原始问题**：之前的代码在内核配置为小于 48 位的 VA 大小时，`kvm_compute_layout()` 中计算的 `hyp_physvirt_offset` 和 `kvm_mmu_init()` 中的 VA 大小计算会出现不一致，可能导致映射失败。

**历史讨论要点**：虽然没有详细的历史讨论记录，但可以推测，此问题的根源在于内存布局和 MMU 初始化之间的协同不足，导致在不同配置下的 VA 大小计算不一致。

**本周新讨论与进展**：Petteri Kangaslampi 提出了一个重构的补丁，确保在所有相关代码路径中使用相同的 VA 大小。该补丁已经在 6.19-rc4 版本上进行了测试，并得到了其他开发者的支持。Vincent Donnefort 进行了测试确认，Marc Zyngier 则表示已将补丁应用到下一步开发中。补丁的主要改动包括在多个文件中对 VA 大小的计算进行统一，避免了之前的潜在映射问题。

#### 📝 邮件列表

1. **[01-13 19:44]** [PATCH v2 0/1] KVM: arm64: Calculate hyp VA size only once
   - 发件人: Petteri Kangaslampi <pekangas@google.com>
2. **[01-13 19:44]** [PATCH v2 1/1] KVM: arm64: Calculate hyp VA size only once
   - 发件人: Petteri Kangaslampi <pekangas@google.com>
3. **[01-14 09:27]** Re: [PATCH v2 1/1] KVM: arm64: Calculate hyp VA size only once
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[01-14 10:51]** Re: [PATCH v2 0/1] KVM: arm64: Calculate hyp VA size only once
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH v2 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 6 Jan 2026 18:00:22 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 在 arm64 架构下的 vGIC-v3 的一个补丁（patch），该补丁旨在切换到使用生成的 ICH_VMCR_EL2。历史讨论中，参与者 Jonathan Cameron 和 Sascha Bischoff 针对补丁的实现细节进行了深入探讨，主要集中在使用 _MASK 版本与不带 _MASK 的定义之间的一致性问题。Sascha 最终决定在 FIELD_x() 操作中使用不带 _MASK 的版本，而在明确作为掩码使用时则使用 _MASK 版本，以提高代码的清晰度。

在本周的新讨论中，Jonathan 对于生成的头文件中同时存在带 _MASK 和不带 _MASK 的定义表示质疑，认为后者没有实际价值，并担心未来的补丁可能会混淆这两者，导致更多的审查反馈。整体来看，讨论围绕代码一致性和清晰性展开，尽管存在不同的观点，但参与者们都在积极寻求最佳实践以改进代码质量。

#### 📝 邮件列表

1. **[01-06 18:00]** Re: [PATCH v2 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
2. **[01-07 10:55]** Re: [PATCH v2 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[01-09 16:57]** Re: [PATCH v2 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[01-12 12:41]** Re: [PATCH v2 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>

---

### Thread 13: [PATCH v5 00/24] ARM64 PMU Partitioning

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 15 Jan 2026 13:02:54 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 ARM64 PMU（性能监控单元）分区的补丁（PATCH v5 00/24）。该补丁旨在实现更动态的主机计数器保留机制，以便在虚拟化环境中更有效地管理性能监控事件。

在历史讨论中，参与者探讨了如何使主机计数器的保留不再依赖于命令行选项，而是能够根据实际情况动态调整。Perf 工具已经支持将事件固定到特定 CPU，因此在驱动程序中处理某些计数器不可用的情况应该是可行的。

在本周的新讨论中，Will Deacon 提出了建议，认为在进入虚拟机时应动态调整主机计数器，以确保主机上下文中始终可以访问完整的计数器范围。Colton Lewis 则提出了一些后续问题，包括如何处理真实事件占用计数器的情况、是否存在不干扰硬件的假事件类型，以及是否有现成的示例代码可以参考。这些讨论表明，参与者们在积极探索如何实现补丁中的动态计数器管理功能。

#### 📝 邮件列表

1. **[01-15 13:02]** Re: [PATCH v5 00/24] ARM64 PMU Partitioning
   - 发件人: Will Deacon <will@kernel.org>
2. **[01-15 18:09]** Re: [PATCH v5 00/24] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

### Thread 14: [PATCH v4 0/5] KVM: selftests: Alignment fixes and arm64 MMU cleanup

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  9 Jan 2026 08:22:13 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 自测的补丁系列，主要集中在内存对齐修复和 arm64 MMU 清理。

**原始 patch/问题的内容**：
Fuad Tabba 提出的补丁系列（[PATCH v4 0/5]）旨在修复 KVM 自测中的内存对齐错误，增强 arm64 MMU 配置，并解决一些文档问题。具体来说，该系列补丁明确禁用了未使用的上层虚拟地址范围（TTBR1）的翻译表遍历，以避免潜在的未初始化问题。

**之前讨论要点**：
在历史讨论中，补丁的主要改动包括将 `page_align()` 重命名为 `vm_page_align()`，并强调了对 arm64 的内存管理单元配置进行硬化的必要性。讨论中提到，保持 TTBR1 未初始化但仍处于活动状态可能导致问题，因此需要进行调整。

**本周的新讨论、进展或结论**：
在本周的讨论中，Marc Zyngier 确认已将该补丁系列应用到下一个版本中，并列出了每个补丁的提交信息。这表明补丁已获得认可并将进入后续的开发流程，进一步推动了 KVM 自测的改进。

#### 📝 邮件列表

1. **[01-09 08:22]** [PATCH v4 0/5] KVM: selftests: Alignment fixes and arm64 MMU cleanup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[01-15 13:44]** Re: [PATCH v4 0/5] KVM: selftests: Alignment fixes and arm64 MMU cleanup
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH v4 0/9] KVM: arm64: Add support for FEAT_IDST

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  8 Jan 2026 17:32:24 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上添加对 ARMv8.4 中引入的 FEAT_IDST 特性的支持。该特性允许在硬件未实现的情况下对 ID 寄存器进行捕获，涉及的寄存器包括 GMID_EL1、CCSIDR2_EL1 和 SMIDR_EL1。

在历史讨论中，Marc Zyngier 提出了一个补丁（PATCH v4 0/9），旨在通过特定方式处理这些寄存器，并实现 GMID_EL1 的支持。补丁的目标是确保即使这些特性在主机上存在，也不会暴露给虚拟机（guest）。

在本周的新讨论中，Marc Zyngier 更新了补丁的进展，确认已将其应用到下一个版本中，并列出了具体的提交内容，包括对 ID_AA64MMFR2_EL1.IDS 描述的重绘、GMID_EL1 的捕获路由、通用同步异常注入原语的添加等。这些提交为实现 FEAT_IDST 特性提供了必要的支持，确保了在缺乏特定处理程序的情况下也能处理相关寄存器。整体来看，讨论进展顺利，补丁已成功集成。

#### 📝 邮件列表

1. **[01-08 17:32]** [PATCH v4 0/9] KVM: arm64: Add support for FEAT_IDST
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-15 12:07]** Re: [PATCH v4 0/9] KVM: arm64: Add support for FEAT_IDST
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH] KVM: arm64: fix missing <asm/stackpage/nvhe.h> include

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 12 Jan 2026 16:04:13 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（内核虚拟机）在 arm64 架构下的补丁，旨在修复缺失的头文件包含问题。具体补丁内容是添加对 `<asm/stacktrace/nvhe.h>` 的引用，以解决在 `arch/arm64/kvm/arm.c` 文件中出现的警告，提示符号 `kvm_arm_hyp_stack_base` 未被声明。

在历史讨论中没有相关内容，但本周的讨论中，Ben Dooks 提出了这个补丁，并详细说明了其目的和修复的警告信息。随后，Marc Zyngier 对该补丁表示认可，并确认已将其应用到下一个版本中。

总结来说，此次讨论的核心是通过补丁修复了 KVM arm64 代码中的一个包含问题，确保了符号的正确声明，并得到了开发者的及时反馈和采纳。

#### 📝 邮件列表

1. **[01-12 16:04]** [PATCH] KVM: arm64: fix missing <asm/stackpage/nvhe.h> include
   - 发件人: Ben Dooks <ben.dooks@codethink.co.uk>
2. **[01-14 11:24]** Re: [PATCH] KVM: arm64: fix missing <asm/stackpage/nvhe.h> include
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 17: [PATCH v4 00/21] KVM: selftests: Add Nested NPT support

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 30 Dec 2025 15:01:29 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）自测试的补丁系列，主题为“添加嵌套 NPT（Nested Page Table）支持”。该补丁由 Yosry 提出，旨在扩展现有的 vmx_dirty_log_test 和 kvm_dirty_log_test，以支持嵌套 SVM（Secure Virtual Machine）。

在历史讨论中，参与者 Sean Christopherson 表达了对最后一个补丁的担忧，认为它可能在内存压力大的情况下导致测试不稳定，但他倾向于在没有明确证据的情况下继续推进该补丁。

在本周的新讨论中，Sean Christopherson 更新了进展，表示已应用除最后一个补丁外的所有补丁，并计划单独发布该补丁的新版本。他还修复了“添加嵌套 NPT 支持”中的一个错误。此外，他列出了已应用的补丁，包括对 KVM 自测试的多个改进和重命名操作。

总体来看，讨论集中在增强 KVM 的嵌套 NPT 支持及其自测试的稳定性和有效性上，进展顺利，除了最后一个补丁外，其他补丁已被接受。

#### 📝 邮件列表

1. **[12-30 15:01]** [PATCH v4 00/21] KVM: selftests: Add Nested NPT support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[01-12 09:38]** Re: [PATCH v4 00/21] KVM: selftests: Add Nested NPT support
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 18: [PATCH kvmtool v4 6/7] arm64: Generate HYP timer interrupt
 specifiers

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 16 Jan 2026 18:14:19 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM 工具的补丁，具体内容为“arm64: 生成 HYP 定时器中断说明符”。这是一个针对 ARM64 架构的补丁，旨在改进 HYP 模式下的定时器中断处理。

在历史讨论中，没有提供具体的背景信息，因此我们无法得知该补丁的详细讨论内容或之前的争议点。

在本周的新讨论中，参与者 Sascha Bischoff 对该补丁进行了审核，并表示认可，附上了“Reviewed-by”的标记。这表明该补丁得到了积极的反馈，可能会在后续版本中被采纳。

总体来看，本周的讨论主要集中在对补丁的审核和认可上，显示出该补丁在社区中的接受度。

#### 📝 邮件列表

1. **[01-16 18:14]** Re: [PATCH kvmtool v4 6/7] arm64: Generate HYP timer interrupt
 specifiers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 19: [PATCH kvmtool v4 4/7] arm64: Add counter offset control

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 16 Jan 2026 18:13:15 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM 工具的补丁，具体内容为“arm64: 添加计数器偏移控制”。该补丁旨在增强 ARM64 架构下 KVM 工具的功能，允许用户更灵活地控制计数器的偏移。

在历史讨论中，邮件列表并没有提供详细的背景信息或之前的讨论内容，因此我们无法得知该补丁的具体背景或先前的争议。

在本周的新讨论中，参与者 Sascha Bischoff 对该补丁进行了审查，并表示支持，确认了补丁的有效性，标记为“Reviewed-by”。这表明该补丁得到了认可，并可能会在后续版本中被采纳。

总体来看，本周的讨论主要集中在对补丁的审查和认可上，未涉及其他技术细节或争议。

#### 📝 邮件列表

1. **[01-16 18:13]** Re: [PATCH kvmtool v4 4/7] arm64: Add counter offset control
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 20: [PATCH kvmtool v4 5/7] arm64: Add FEAT_E2H0 support

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 16 Jan 2026 18:12:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 工具中添加对 ARM64 架构的 FEAT_E2H0 支持的补丁（patch）。该补丁的目的是增强 KVM 工具对 ARM64 虚拟化特性的支持。

在之前的讨论中，虽然没有详细记录，但可以推测该补丁的背景涉及对 ARM64 架构虚拟化功能的扩展，特别是与嵌套虚拟化相关的特性。

在本周的新讨论中，参与者 Sascha Bischoff 对补丁进行了审查，并表示支持（Reviewed-by）。他提出了一个建议，即在使用 `--e2h0` 参数时，如果没有同时设置 `--nested`，则应打印出相关提示信息，以避免用户误解该参数的效果。此外，他对将 `--e2h0` 参数强制与 `--nested` 参数关联的提议表示不赞同。

总体来看，本周的讨论集中在用户体验和参数使用的明确性上，确保用户在使用 KVM 工具时能够清楚理解各个参数的作用。

#### 📝 邮件列表

1. **[01-16 18:12]** Re: [PATCH kvmtool v4 5/7] arm64: Add FEAT_E2H0 support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 21: [PATCH kvmtool v4 3/7] arm64: nested: Add support for setting
 maintenance IRQ

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 16 Jan 2026 18:10:11 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 工具中为 ARM64 架构的嵌套虚拟化添加设置维护中断（maintenance IRQ）支持的补丁（patch）[PATCH kvmtool v4 3/7]。该补丁旨在解决在使用 GICv3 时，嵌套虚拟化功能无法正确设置维护中断的问题。

在之前的讨论中，Andre Przywara 提出了对嵌套虚拟化的支持存在缺陷，特别是如果没有能力设置维护中断，可能会导致功能不正常。他认为在这种情况下应该返回错误，以避免生成不必要的属性。

本周的讨论中，Sascha Bischoff 对此进行了回应，强调如果无法设置维护中断，仍然会生成该属性，这可能会引发混淆。他的观点是，应该在缺少设置能力时明确返回错误，以提高代码的健壮性和可维护性。

总体而言，本周的讨论集中在如何处理维护中断的设置问题上，强调了在嵌套虚拟化中确保正确性的重要性。

#### 📝 邮件列表

1. **[01-16 18:10]** Re: [PATCH kvmtool v4 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 22: [PATCH kvmtool v4 2/7] arm64: Initial nested virt support

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 16 Jan 2026 18:07:21 +0000

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH kvmtool v4 2/7] arm64: Initial nested virt support”，主要涉及对 ARM64 架构下嵌套虚拟化支持的初步补丁。

在本周的新讨论中，参与者 Andre Przywara 对该补丁表示认可，并指出该补丁已在 GICv5 硬件（FVP）上进行了测试，具体是针对 GICv3 客户机在 GICv5 主机上的支持（FEAT_GCIE_LEGACY）。Sascha Bischoff 也对该补丁进行了审核，并给予了“Reviewed-by”标记，表明他对补丁的认可和支持。

总结来看，本周的讨论主要集中在对补丁的认可和测试结果上，显示出该补丁在嵌套虚拟化支持方面的有效性和可靠性。

#### 📝 邮件列表

1. **[01-16 18:07]** Re: [PATCH kvmtool v4 2/7] arm64: Initial nested virt support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 23: [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 16 Jan 2026 07:32:47 -0800

#### 🤖 AI 总结

本邮件主题为“[PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs”，主要讨论了在 KVM 中添加对中介虚拟性能监控单元（vPMUs）的支持。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁系列旨在增强 KVM 对虚拟化环境中性能监控的支持，特别是针对 Intel 和 AMD 处理器的中介 PMU 需求和约束。

本周的讨论中，Sean Christopherson 提到已经将相关的 KVM 补丁应用到 kvm-x86 的 PMU 中，并列出了多个补丁的链接和状态。这些补丁包括注册性能回调的简化包装、实现 Intel 和 AMD 的中介 PMU 需求、处理 PMU 事件选择器的更新等。具体补丁如 [14/44] 和 [17/44] 等，均已成功合并或修复，显示出补丁的逐步落实和进展。

总体来看，本周的讨论表明该补丁系列正在顺利推进，KVM 对中介 vPMUs 的支持正在逐步实现。

#### 📝 邮件列表

1. **[01-16 07:32]** Re: [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 24: [PATCH] KVM: arm64: Fix error checking for FFA_VERSION

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 16 Jan 2026 09:48:14 +0000

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: Fix error checking for FFA_VERSION”，主要讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 FFA_VERSION 错误检查的修复。

在历史讨论中，邮件列表没有相关的背景讨论记录，因此我们无法提供更多的上下文信息。

在本周的新讨论中，Marc Zyngier 回复了 Kornel Dulęba 的补丁，确认该补丁已被应用到下一个版本中。补丁的提交 ID 为 582234b0d8419e0b6cbfd87ae3f80568c8d0917e，表明该修复已被正式纳入代码库。

总结来看，本周的讨论主要集中在确认补丁的应用上，未涉及其他新问题或进一步的讨论。

#### 📝 邮件列表

1. **[01-16 09:48]** Re: [PATCH] KVM: arm64: Fix error checking for FFA_VERSION
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 25: [PATCH v2 0/6] KVM: arm64: VTCR_EL2 conversion to feature dependency framework

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 15 Jan 2026 11:49:06 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 VTCR_EL2 寄存器转换为特性依赖框架的补丁（PATCH v2 0/6）。该补丁系列旨在改进虚拟化环境下的寄存器管理和特性支持。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的目标是通过将 VTCR_EL2 寄存器的处理与特性依赖框架相结合，提升 KVM 的灵活性和可维护性。

在本周的新讨论中，Marc Zyngier 确认已将该补丁应用到下一个开发周期，并列出了补丁的具体提交内容，包括将 ID_AA64MMFR0_EL1.TGRAN{4,16,64}_2 转换为无符号枚举、将 VTCR_EL2 转换为系统寄存器基础设施、以及处理 RES1 位和配置驱动的清理等。这些进展表明补丁已获得认可，并将进一步推动 KVM 在 arm64 上的优化。

#### 📝 邮件列表

1. **[01-15 11:49]** Re: [PATCH v2 0/6] KVM: arm64: VTCR_EL2 conversion to feature dependency framework
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 26: [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 12 Jan 2026 09:38:38 -0800

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: Remove subtle 'struct kvm_stats_desc' pseudo-overlay”，主要讨论了对 KVM（Kernel-based Virtual Machine）的一项补丁。该补丁的内容是移除一个名为“struct kvm_stats_desc”的伪叠加结构，目的是简化代码并提高可读性。

在历史讨论中并未提供具体的背景信息或之前的讨论要点，因此我们无法了解该补丁的详细背景或其引发的争议。

在本周的新讨论中，参与者 Sean Christopherson 提到该补丁已成功应用于 kvm-x86 的通用代码中，并对此表示感谢。补丁的提交链接也被附上，表明该项工作已经得到认可并实施。

总结而言，本周的讨论主要集中在补丁的应用和确认上，未涉及其他争议或深入讨论。

#### 📝 邮件列表

1. **[01-12 09:38]** Re: [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay
   - 发件人: Sean Christopherson <seanjc@google.com>

---

## 📌 RFC

共 4 个 thread

---

### Thread 1: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 9 Jan 2026 16:29:50 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的配置选项的补丁，主题为“[RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig option”。该补丁旨在添加 CONFIG_KVM_ARM_SPE 选项，以便更好地支持 ARM SPE（Statistical Profiling Extension）。

在历史讨论中，Alexandru Elisei 提出了对补丁的担忧，认为强制将其编译为内置模块可能会影响用户的采用率。他建议在无法启用时提供调试信息，以帮助用户理解问题。

在本周的新讨论中，Alexandru 和 James Clark 继续探讨了补丁的实现细节。Alexandru 表示，KVM 需要处理与 SPE 驱动之间的依赖关系，尤其是在中断和系统文件的创建方面。James 也指出，缺乏警告信息可能会导致用户在配置时遇到困难。最终，Alexandru 提出了一个改进方案，建议导出 `kvm_host_spe_init()` 函数，使得 SPE 驱动可以作为模块构建，同时确保 VM 只有在驱动加载后才能使用 SPE。这一改动旨在改善用户的采用体验。整体来看，讨论集中在如何平衡模块化与用户友好性之间的关系。

#### 📝 邮件列表

1. **[01-09 16:29]** Re: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option
   - 发件人: James Clark <james.clark@linaro.org>
2. **[01-12 11:26]** Re: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[01-12 12:09]** Re: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option
   - 发件人: James Clark <james.clark@linaro.org>
4. **[01-12 12:14]** Re: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option
   - 发件人: James Clark <james.clark@linaro.org>
5. **[01-12 15:18]** Re: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[01-13 10:25]** Re: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[01-13 15:00]** Re: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option
   - 发件人: James Clark <james.clark@linaro.org>
8. **[01-13 17:03]** Re: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 2: [RFC PATCH v6 19/35] KVM: arm64: Trap PMBIDR_EL1 and PMSIDR_EL1

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 9 Jan 2026 16:29:37 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 PMBIDR_EL1 和 PMSIDR_EL1 寄存器的处理。原始的 RFC PATCH v6 19/35 提出了在虚拟化环境中捕获这两个寄存器的需求，目的是为了能够报告不同的 PMBIDR 值。

在历史讨论中，Alexandru Elisei 提出，只有在需要报告与硬件不同的 PMBIDR 值时，才需要进行捕获；如果硬件值已经符合需求，则不一定需要此功能，可能可以作为后续的扩展。

在本周的新讨论中，Alexandru 和 James Clark 继续探讨了该补丁的必要性。Alexandru 指出，PMBIDR 中的值为 0（表示“无限制”）是一个有效值，只有在值不匹配时才需要捕获。他还提到，可以通过尝试设置限制指针并查看缓冲管理错误代码来探测最大缓冲区大小。此外，James 提出可以为设置最大缓冲区大小添加新功能，但这可能会影响到某些硬件的兼容性。最终，Alexandru 表示可以等待其他用户的反馈再决定是否进一步讨论此功能的实现。

总体来看，本周的讨论主要集中在对补丁必要性的深入分析及其对不同硬件的兼容性考虑上。

#### 📝 邮件列表

1. **[01-09 16:29]** Re: [RFC PATCH v6 19/35] KVM: arm64: Trap PMBIDR_EL1 and PMSIDR_EL1
   - 发件人: James Clark <james.clark@linaro.org>
2. **[01-12 11:28]** Re: [RFC PATCH v6 19/35] KVM: arm64: Trap PMBIDR_EL1 and PMSIDR_EL1
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[01-12 11:54]** Re: [RFC PATCH v6 19/35] KVM: arm64: Trap PMBIDR_EL1 and PMSIDR_EL1
   - 发件人: James Clark <james.clark@linaro.org>
4. **[01-13 12:48]** Re: [RFC PATCH v6 19/35] KVM: arm64: Trap PMBIDR_EL1 and PMSIDR_EL1
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
5. **[01-13 14:22]** Re: [RFC PATCH v6 19/35] KVM: arm64: Trap PMBIDR_EL1 and PMSIDR_EL1
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 3: [RFC PATCH v6 14/35] KVM: arm64: Add SPE VCPU device attribute to
 set the max buffer size

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 9 Jan 2026 16:29:43 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中为 arm64 架构添加 SPE（Statistical Profiling Extension）VCPU 设备属性，以设定最大缓冲区大小的补丁（patch）。该补丁的目的是允许用户设置一个不超过物理 SPU 实例支持的最大值的缓冲区大小。

在历史讨论中，参与者 James Clark 提到他曾遇到过与缓冲区大小相关的问题，但在尝试不同的大小后，这个问题似乎消失了。他认为可能是由于某种错误或环境因素导致的，因此不需要过于关注。

本周的新讨论中，Alexandru Elisei 和 James Clark 继续探讨了该补丁的实现细节。Alex 表示将修改注释，说明选择 4MiB 作为默认值的原因，并讨论了在不同虚拟化环境下，物理实例的硬件值可能会变化。James 认为，虽然 kvmtool 目前不用于生产，但设定一个合理的默认值是有益的，以便于其他工具或脚本使用。Alex 进一步强调，设置最大缓冲区大小的属性是为了在内存受限的环境中使用 SPE，因此需要合理考虑默认值的选择。

总体来看，本周讨论主要集中在补丁的实现细节和默认值的合理性上，参与者们达成了一致，即需要确保在不同环境下的兼容性和合理性。

#### 📝 邮件列表

1. **[01-09 16:29]** Re: [RFC PATCH v6 14/35] KVM: arm64: Add SPE VCPU device attribute to
 set the max buffer size
   - 发件人: James Clark <james.clark@linaro.org>
2. **[01-12 11:28]** Re: [RFC PATCH v6 14/35] KVM: arm64: Add SPE VCPU device attribute
 to set the max buffer size
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[01-12 11:50]** Re: [RFC PATCH v6 14/35] KVM: arm64: Add SPE VCPU device attribute to
 set the max buffer size
   - 发件人: James Clark <james.clark@linaro.org>
4. **[01-12 14:03]** Re: [RFC PATCH v6 14/35] KVM: arm64: Add SPE VCPU device attribute
 to set the max buffer size
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 4: [RFC PATCH v6 29/35] KVM: arm64: Pin the SPE buffer in the host
 and map it at stage 2

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 9 Jan 2026 16:29:33 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 SPE（Statistical Profiling Extension）缓冲区的管理，具体是将其固定在主机内存中并在第二阶段进行映射。

**原始 patch/问题的内容**：
该补丁旨在解决在目标进程切换时，SPE 缓冲区频繁启用和禁用的问题，这导致了性能下降，尤其是在使用较大缓冲区时。

**之前讨论要点**：
在历史讨论中，Alexandru Elisei 提出，当前的实现使得在正常的性能命令下，SPE 缓冲区的使用变得几乎不可用。他建议引入某种启发式方法，以避免在没有实际变化的情况下频繁地固定和释放缓冲区。

**本周的新讨论、进展或结论**：
本周的讨论中，James Clark 表示能够重现性能问题，并提出可能的解决方案，包括在缓冲区禁用时保持内存固定，并在需要时才释放内存。他还考虑引入定时器和内存老化机制来管理缓冲区的固定状态。Alexandru Elisei 反驳了限制缓冲区大小的建议，指出这会影响希望使用较大缓冲区的用户，特别是在快照模式下，较大的缓冲区对于捕获执行历史至关重要。讨论中还提到，当前的实现即使在默认的 4MB 缓冲区下也会显著增加上下文切换的时间，影响整体性能，表明需要进一步的基准测试和优化。

#### 📝 邮件列表

1. **[01-09 16:29]** Re: [RFC PATCH v6 29/35] KVM: arm64: Pin the SPE buffer in the host
 and map it at stage 2
   - 发件人: James Clark <james.clark@linaro.org>
2. **[01-12 12:01]** Re: [RFC PATCH v6 29/35] KVM: arm64: Pin the SPE buffer in the host
 and map it at stage 2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[01-13 14:18]** Re: [RFC PATCH v6 29/35] KVM: arm64: Pin the SPE buffer in the host
 and map it at stage 2
   - 发件人: James Clark <james.clark@linaro.org>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v5 00/11] arm64: EL2 support

**📧 邮件数**: 19 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 14 Jan 2026 11:56:52 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM 单元测试的 EL2 支持的补丁系列（PATCH v5 00/11）。该补丁的主要目标是使 KVM 单元测试能够在 EL2 级别运行，包含了多项改进和修复。

在历史讨论中，补丁的背景和目标已被明确，主要是为 KVM 单元测试添加对 EL2 的支持。补丁中包含了对环境变量的修改，使其支持 EL2=1、y、Y 的设置，并对自测进行了更新，以适应在 EL2 运行的需求。

本周的新讨论中，Joey Gouly 提出了具体的补丁内容，包括设置 SCTLR_EL1 的已知值、在启动时从 EL2 降级到 EL1、初始化 EL2 环境、使用虚拟化定时器等。参与者对补丁进行了审查，部分补丁已获得认可。然而，Andrew Jones 提到在使用 EL2=1 时，测试出现了一些问题，如定时器测试超时、调试断点和观察点测试失败等，建议在合并前解决这些问题或进行适当的跳过处理。此外，讨论中还提到需要在 CI 测试中添加 EL2=y 的测试，以确保新功能的稳定性。

总结而言，尽管补丁系列在功能上有所进展，但仍需解决现有的测试失败问题，以确保在 EL2 环境下的稳定性和可靠性。

#### 📝 邮件列表

1. **[01-14 11:56]** [kvm-unit-tests PATCH v5 00/11] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[01-14 11:56]** [kvm-unit-tests PATCH v5 01/11] arm64: set SCTLR_EL1 to a known value for secondary cores
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[01-14 11:56]** [kvm-unit-tests PATCH v5 02/11] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[01-14 11:56]** [kvm-unit-tests PATCH v5 03/11] arm64: efi: initialise SCTLR_ELx fully
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[01-14 11:56]** [kvm-unit-tests PATCH v5 04/11] arm64: efi: initialise the EL
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[01-14 11:56]** [kvm-unit-tests PATCH v5 05/11] arm64: timer: use hypervisor timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
7. **[01-14 11:56]** [kvm-unit-tests PATCH v5 06/11] arm64: micro-bench: fix timer IRQ
   - 发件人: Joey Gouly <joey.gouly@arm.com>
8. **[01-14 11:56]** [kvm-unit-tests PATCH v5 07/11] arm64: micro-bench: use smc when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[01-14 11:57]** [kvm-unit-tests PATCH v5 08/11] arm64: selftest: update test for running at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
10. **[01-14 11:57]** [kvm-unit-tests PATCH v5 09/11] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
11. **[01-14 11:57]** [kvm-unit-tests PATCH v5 10/11] arm64: run at EL2 if supported
   - 发件人: Joey Gouly <joey.gouly@arm.com>
12. **[01-14 11:57]** [kvm-unit-tests PATCH v5 11/11] arm64: add EL2 environment variable
   - 发件人: Joey Gouly <joey.gouly@arm.com>
13. **[01-15 11:30]** Re: [kvm-unit-tests PATCH v5 08/11] arm64: selftest: update test for
 running at EL2
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
14. **[01-15 11:40]** Re: [kvm-unit-tests PATCH v5 00/11] arm64: EL2 support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
15. **[01-15 11:44]** Re: [kvm-unit-tests PATCH v5 11/11] arm64: add EL2 environment
 variable
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
16. **[01-15 11:49]** Re: [kvm-unit-tests PATCH v5 00/11] arm64: EL2 support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
17. **[01-15 18:51]** Re: [kvm-unit-tests PATCH v5 00/11] arm64: EL2 support
   - 发件人: Eric Auger <eric.auger@redhat.com>
18. **[01-15 22:32]** Re: [kvm-unit-tests PATCH v5 00/11] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
19. **[01-15 18:11]** Re: [kvm-unit-tests PATCH v5 00/11] arm64: EL2 support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 2: KVM/arm64 fixes for 6.19

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 15 Jan 2026 01:30:25 -0800

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM/arm64 的修复补丁，主要集中在 6.19 版本的改进。

1. **原始补丁内容**：Oliver Upton 提交了一组针对 KVM/arm64 的修复补丁，旨在解决在非标准配置（如 pKVM、hVHE 和嵌套虚拟化）下存在的问题。补丁包括确保 pKVM 故障处理程序的早期返回语义、修复在未设置 CONFIG_ARM64_PAN 时内核使用来宾的 PAN 值的情况、以及在设置访问标志时尊重底层阶段 2 的访问权限等。

2. **之前讨论要点**：该邮件线程没有提供历史讨论的内容，所有讨论均为本周的新进展。

3. **本周新讨论及进展**：Oliver 提交的补丁已被 Marc Zyngier 接受，并计划作为初步合并到 kvmarm/next 分支中，因为 Marc 有一些依赖于此补丁的后续工作。邮件中详细列出了补丁的具体修改内容，包括对多个文件的插入和删除操作，显示出对 KVM/arm64 的持续关注和改进。

总的来说，本周的讨论集中在 KVM/arm64 的修复补丁上，强调了对特定配置的支持和错误修复，标志着向 6.19 版本的顺利推进。

#### 📝 邮件列表

1. **[01-15 01:30]** KVM/arm64 fixes for 6.19
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[01-15 10:04]** Re: KVM/arm64 fixes for 6.19
   - 发件人: Marc Zyngier <maz@kernel.org>

---

