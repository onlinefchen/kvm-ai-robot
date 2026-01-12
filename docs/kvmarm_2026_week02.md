# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2026-01-12 00:25:47

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 405
- **总 Thread 数**: 38
- **大型 Thread** (>20封): 5 个

### 分类分布

- **PATCH**: 31 threads (382 邮件)
- **RFC**: 6 threads (7 邮件)
- **Other**: 1 threads (16 邮件)

---

## 📌 PATCH

共 31 个 thread

---

### Thread 1: [PATCH v2 03/45] arm_mpam: Use non-atomic bitops when modifying
 feature bitmap

**📧 邮件数**: 65 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 5 Jan 2026 16:34:37 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 ARM MPAM（Memory Partitioning and Monitoring）相关的多个补丁（PATCH v2 03/45及后续补丁）。主要内容集中在如何在修改特性位图时使用非原子位操作，以避免在结构体对齐要求不满足时引发的问题。

在历史讨论中，参与者对使用非原子操作表示了关注，认为虽然不太可能会“升级”这些操作，但在代码中添加注释以解释为何选择非原子版本是有必要的。Jonathan Cameron 对补丁进行了审查并表示认可。

本周的新讨论中，Ben Horgan 和 Jonathan Cameron 继续对多个补丁进行审查和修改。Ben 针对补丁中的一些实现细节进行了更新，例如在访问特定字段时使用 `READ_ONCE()` 和 `WRITE_ONCE()`，以确保数据一致性。此外，讨论中还涉及到如何处理 MPAM 寄存器的上下文切换、初始化和配置等问题。Shaopeng Tan 提出了对某些补丁的具体建议，进一步推动了讨论的深入。

总体来看，本周的讨论集中在补丁的细节审查、代码清晰度的提升以及对 MPAM 功能实现的具体建议上，显示出参与者对代码质量和功能实现的高度关注。

#### 📝 邮件列表

1. **[01-05 16:34]** Re: [PATCH v2 03/45] arm_mpam: Use non-atomic bitops when modifying
 feature bitmap
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
2. **[01-05 16:36]** Re: [PATCH v2 04/45] arm64/sysreg: Add MPAMSM_EL1 register
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
3. **[01-05 16:43]** Re: [PATCH v2 05/45] KVM: arm64: Preserve host MPAM configuration
 when changing traps
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
4. **[01-05 16:47]** Re: [PATCH v2 06/45] KVM: arm64: Make MPAMSM_EL1 accesses UNDEF
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
5. **[01-05 16:57]** Re: [PATCH v2 06/45] KVM: arm64: Make MPAMSM_EL1 accesses UNDEF
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[01-05 17:04]** Re: [PATCH v2 07/45] arm64: mpam: Context switch the MPAM registers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
7. **[01-05 17:06]** Re: [PATCH v2 08/45] arm64: mpam: Re-initialise MPAM regs when CPU
 comes online
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
8. **[01-05 17:08]** Re: [PATCH v2 09/45] arm64: mpam: Advertise the CPUs MPAM limits to
 the driver
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
9. **[01-05 17:09]** Re: [PATCH v2 10/45] arm64: mpam: Add cpu_pm notifier to restore
 MPAM sysregs
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
10. **[01-05 17:20]** Re: [PATCH v2 11/45] arm64: mpam: Initialise and context switch the
 MPAMSM_EL1 register
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
11. **[01-05 17:21]** Re: [PATCH v2 12/45] arm64: mpam: Add helpers to change a task or
 cpu's MPAM PARTID/PMG values
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
12. **[01-05 17:40]** Re: [PATCH v2 15/45] arm_mpam: resctrl: Add boilerplate cpuhp and
 domain allocation
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
13. **[01-05 17:42]** Re: [PATCH v2 16/45] arm_mpam: resctrl: Sort the order of the
 domain lists
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
14. **[01-05 17:46]** Re: [PATCH v2 17/45] arm_mpam: resctrl: Pick the caches we will use
 as resctrl resources
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
15. **[01-05 17:51]** Re: [PATCH v2 18/45] arm_mpam: resctrl: Implement
 resctrl_arch_reset_all_ctrls()
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
16. **[01-05 17:53]** Re: [PATCH v2 19/45] arm_mpam: resctrl: Add
 resctrl_arch_get_config()
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
17. **[01-05 17:58]** Re: [PATCH v2 20/45] arm_mpam: resctrl: Implement helpers to update
 configuration
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
18. **[01-05 18:02]** Re: [PATCH v2 21/45] arm_mpam: resctrl: Add plumbing against arm64
 task and cpu hooks
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
19. **[01-05 18:07]** Re: [PATCH v2 22/45] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
20. **[01-06 11:11]** Re: [PATCH v2 03/45] arm_mpam: Use non-atomic bitops when modifying
 feature bitmap
   - 发件人: Ben Horgan <ben.horgan@arm.com>
21. **[01-06 11:14]** Re: [PATCH v2 07/45] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
22. **[01-06 11:17]** Re: [PATCH v2 15/45] arm_mpam: resctrl: Add boilerplate cpuhp and
 domain allocation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
23. **[01-06 11:19]** Re: [PATCH v2 18/45] arm_mpam: resctrl: Implement
 resctrl_arch_reset_all_ctrls()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
24. **[01-06 11:21]** Re: [PATCH v2 23/45] arm_mpam: resctrl: Add rmid index helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
25. **[01-06 11:21]** Re: [PATCH v2 22/45] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
26. **[01-06 11:33]** Re: [PATCH v2 23/45] arm_mpam: resctrl: Add rmid index helpers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
27. **[01-06 11:55]** Re: [PATCH v2 24/45] arm_mpam: resctrl: Convert to/from MPAMs
 fixed-point formats
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
28. **[01-06 12:19]** Re: [PATCH v2 25/45] arm_mpam: resctrl: Add support for 'MB'
 resource
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
29. **[01-06 12:30]** Re: [PATCH v2 26/45] arm_mpam: resctrl: Add kunit test for control
 format conversions
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
30. **[01-06 12:40]** Re: [PATCH v2 27/45] arm_mpam: resctrl: Add support for csu
 counters
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
31. **[01-06 14:01]** Re: [PATCH v2 28/45] arm_mpam: resctrl: Pick classes for use as mbm
 counters
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
32. **[01-06 14:03]** Re: [PATCH v2 07/45] arm64: mpam: Context switch the MPAM registers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
33. **[01-06 14:04]** Re: [PATCH v2 23/45] arm_mpam: resctrl: Add rmid index helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
34. **[01-06 14:22]** Re: [PATCH v2 29/45] arm_mpam: resctrl: Pre-allocate free running
 monitors
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
35. **[01-06 14:29]** Re: [PATCH v2 30/45] arm_mpam: resctrl: Pre-allocate assignable
 monitors
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
36. **[01-06 14:33]** Re: [PATCH v2 32/45] arm_mpam: resctrl: Add
 resctrl_arch_config_cntr() for ABMC use
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
37. **[01-06 14:37]** Re: [PATCH v2 33/45] arm_mpam: resctrl: Allow resctrl to allocate
 monitors
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
38. **[01-06 14:43]** Re: [PATCH v2 34/45] arm_mpam: resctrl: Add
 resctrl_arch_rmid_read() and resctrl_arch_reset_rmid()
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
39. **[01-06 14:44]** Re: [PATCH v2 35/45] arm_mpam: resctrl: Add
 resctrl_arch_cntr_read() & resctrl_arch_reset_cntr()
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
40. **[01-06 14:46]** Re: [PATCH v2 36/45] arm_mpam: resctrl: Update the rmid
 reallocation limit
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
41. **[01-06 14:48]** Re: [PATCH v2 37/45] arm_mpam: resctrl: Add empty definitions for
 assorted resctrl functions
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
42. **[01-06 14:49]** Re: [PATCH v2 38/45] arm64: mpam: Select ARCH_HAS_CPU_RESCTRL
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
43. **[01-06 14:58]** Re: [PATCH v2 39/45] arm_mpam: resctrl: Call resctrl_init() on
 platforms that can support resctrl
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
44. **[01-06 15:09]** Re: [PATCH v2 40/45] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
45. **[01-06 15:14]** Re: [PATCH v2 41/45] arm_mpam: Add quirk framework
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
46. **[01-06 15:15]** Re: [PATCH v2 41/45] arm_mpam: Add quirk framework
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
47. **[01-06 15:20]** Re: [PATCH v2 43/45] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
48. **[01-06 15:23]** Re: [PATCH v2 23/45] arm_mpam: resctrl: Add rmid index helpers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
49. **[01-07 14:21]** Re: [PATCH v2 25/45] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
50. **[01-07 15:19]** Re: [PATCH v2 28/45] arm_mpam: resctrl: Pick classes for use as mbm
 counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
51. **[01-08 10:06]** Re: [PATCH v2 07/45] arm64: mpam: Context switch the MPAM registers
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
52. **[01-08 10:18]** Re: [PATCH v2 12/45] arm64: mpam: Add helpers to change a task or
 cpu's MPAM PARTID/PMG values
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
53. **[01-08 10:36]** Re: [PATCH v2 15/45] arm_mpam: resctrl: Add boilerplate cpuhp and
 domain allocation
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
54. **[01-08 10:42]** Re: [PATCH v2 25/45] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
55. **[01-08 10:44]** Re: [PATCH v2 27/45] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
56. **[01-08 10:52]** Re: [PATCH v2 27/45] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
57. **[01-08 14:25]** Re: [PATCH v2 29/45] arm_mpam: resctrl: Pre-allocate free running
 monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
58. **[01-08 14:33]** Re: [PATCH v2 30/45] arm_mpam: resctrl: Pre-allocate assignable
 monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
59. **[01-08 14:53]** Re: [PATCH v2 39/45] arm_mpam: resctrl: Call resctrl_init() on
 platforms that can support resctrl
   - 发件人: Ben Horgan <ben.horgan@arm.com>
60. **[01-08 15:35]** Re: [PATCH v2 40/45] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
61. **[01-08 19:22]** Re: (subset) [PATCH v2 00/45] arm_mpam: Add KVM/arm64 and resctrl
 glue code
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
62. **[01-09 11:45]** Re: [PATCH v2 18/45] arm_mpam: resctrl: Implement resctrl_arch_reset_all_ctrls()
   - 发件人: Zeng Heng <zengheng4@huawei.com>
63. **[01-09 09:28]** Re: [PATCH v2 07/45] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
64. **[01-09 09:37]** Re: [PATCH v2 12/45] arm64: mpam: Add helpers to change a task or
 cpu's MPAM PARTID/PMG values
   - 发件人: Ben Horgan <ben.horgan@arm.com>
65. **[01-09 09:55]** Re: [PATCH v2 15/45] arm_mpam: resctrl: Add boilerplate cpuhp and
 domain allocation
   - 发件人: Ben Horgan <ben.horgan@arm.com>

---

### Thread 2: [PATCH v2 07/36] KVM: arm64: gic: Introduce interrupt type
 helpers

**📧 邮件数**: 62 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 6 Jan 2026 14:51:26 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的 GIC（通用中断控制器）实现的一系列补丁，特别是引入中断类型助手的补丁（PATCH v2 07/36）。

1. **原始补丁内容**：该补丁旨在引入中断类型助手，以便更好地管理 GIC 的中断类型，提升 KVM 对 GICv5 的支持。

2. **之前讨论要点**：在历史讨论中，参与者们对补丁的设计和实现进行了初步的审查，提出了一些命名和实现上的建议。Sascha Bischoff 是主要的提交者，讨论中涉及到对补丁的功能性和代码风格的反馈。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的审查和细节修改上。Joey Gouly 和 Jonathan Cameron 对多个补丁进行了审查，提出了具体的改进建议，例如代码的可读性和一致性问题。Sascha 对这些反馈进行了积极响应，并表示将根据建议进行相应的修改。此外，讨论中还提到了一些补丁的文档化工作，确保相关功能的使用和实现能够被清晰理解。

总体而言，本周的讨论表明补丁系列正在逐步完善，参与者们积极协作以提升代码质量和功能实现的准确性。

#### 📝 邮件列表

1. **[01-06 14:51]** Re: [PATCH v2 07/36] KVM: arm64: gic: Introduce interrupt type
 helpers
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[01-06 15:06]** Re: [PATCH v2 27/36] KVM: arm64: gic-v5: Mandate architected PPI for
 PMU emulation on GICv5
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[01-06 16:06]** Re: [PATCH v2 18/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[01-06 17:23]** Re: [PATCH v2 01/36] KVM: arm64: Account for RES1 bits in
 DECLARE_FEAT_MAP() and co
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
5. **[01-06 18:00]** Re: [PATCH v2 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
6. **[01-06 18:04]** Re: [PATCH v2 18/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[01-06 18:08]** Re: [PATCH v2 05/36] arm64/sysreg: Add GICR CDNMIA encoding
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
8. **[01-06 18:28]** Re: [PATCH v2 04/36] arm64/sysreg: Add remaining GICv5 ICC_ & ICH_
 sysregs for KVM support
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
9. **[01-06 18:34]** Re: [PATCH v2 09/36] KVM: arm64: gic-v5: Detect implemented PPIs on
 boot
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
10. **[01-06 18:43]** Re: [PATCH v2 07/36] KVM: arm64: gic: Introduce interrupt type
 helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
11. **[01-07 08:39]** Re: [PATCH v2 05/36] arm64/sysreg: Add GICR CDNMIA encoding
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[01-07 09:48]** Re: [PATCH v2 27/36] KVM: arm64: gic-v5: Mandate architected PPI for
 PMU emulation on GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[01-07 10:30]** Re: [PATCH v2 08/36] KVM: arm64: Introduce kvm_call_hyp_nvhe_res()
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
14. **[01-07 10:55]** Re: [PATCH v2 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[01-07 10:58]** Re: [PATCH v2 10/36] KVM: arm64: gic-v5: Sanitize
 ID_AA64PFR2_EL1.GCIE
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
16. **[01-07 11:10]** Re: [PATCH v2 12/36] KVM: arm64: gic-v5: Add emulation for
 ICC_IAFFIDR_EL1 accesses
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
17. **[01-07 11:19]** Re: [PATCH v2 11/36] KVM: arm64: gic-v5: Support GICv5 FGTs & FGUs
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
18. **[01-07 11:24]** Re: [PATCH v2 13/36] KVM: arm64: gic: Set vgic_model before initing
 private IRQs
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
19. **[01-07 12:16]** Re: [PATCH v2 16/36] KVM: arm64: gic-v5: Implement direct injection
 of PPIs
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
20. **[01-07 12:22]** Re: [PATCH v2 17/36] KVM: arm64: gic: Introduce irq_queue and
 set_pending_state to irq_ops
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
21. **[01-07 12:28]** Re: [PATCH v2 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put
 and save/restore
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
22. **[01-07 12:50]** Re: [PATCH v2 18/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
23. **[01-07 15:00]** Re: [PATCH v2 19/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
24. **[01-07 15:04]** Re: [PATCH v2 20/36] KVM: arm64: gic-v5: Init Private IRQs (PPIs)
 for GICv5
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
25. **[01-07 15:08]** Re: [PATCH v2 21/36] KVM: arm64: gic-v5: Finalize GICv5 PPIs and
 generate mask
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
26. **[01-07 15:17]** Re: [PATCH v2 22/36] KVM: arm64: gic-v5: Trap and mask guest PPI
 register accesses
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
27. **[01-07 15:29]** Re: [PATCH v2 23/36] KVM: arm64: gic-v5: Support GICv5 interrupts
 with KVM_IRQ_LINE
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
28. **[01-07 15:49]** Re: [PATCH v2 24/36] KVM: arm64: gic-v5: Create, init vgic_v5
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
29. **[01-07 15:51]** Re: [PATCH v2 25/36] KVM: arm64: gic-v5: Reset vcpu state
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
30. **[01-07 16:08]** Re: [PATCH v2 26/36] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
31. **[01-07 16:11]** Re: [PATCH v2 27/36] KVM: arm64: gic-v5: Mandate architected PPI
 for PMU emulation on GICv5
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
32. **[01-07 16:12]** Re: [PATCH v2 28/36] KVM: arm64: gic: Hide GICv5 for protected
 guests
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
33. **[01-07 16:13]** Re: [PATCH v2 29/36] KVM: arm64: gic-v5: Hide FEAT_GCIE from NV
 GICv5 guests
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
34. **[01-07 16:19]** Re: [PATCH v2 30/36] KVM: arm64: gic-v5: Introduce
 kvm_arm_vgic_v5_ops and register them
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
35. **[01-07 16:21]** Re: [PATCH v2 32/36] irqchip/gic-v5: Check if impl is virt capable
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
36. **[01-07 16:25]** Re: [PATCH v2 33/36] KVM: arm64: gic-v5: Probe for GICv5 device
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
37. **[01-07 16:27]** Re: [PATCH v2 34/36] Documentation: KVM: Introduce documentation
 for VGICv5
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
38. **[01-07 16:38]** Re: [PATCH v2 35/36] KVM: arm64: selftests: Introduce a minimal
 GICv5 PPI selftest
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
39. **[01-07 16:51]** Re: [PATCH v2 36/36] KVM: arm64: gic-v5: Communicate
 userspace-drivable PPIs via a UAPI
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
40. **[01-08 09:33]** Re: [PATCH v2 07/36] KVM: arm64: gic: Introduce interrupt type
 helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
41. **[01-08 09:48]** Re: [PATCH v2 08/36] KVM: arm64: Introduce kvm_call_hyp_nvhe_res()
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
42. **[01-08 09:54]** Re: [PATCH v2 10/36] KVM: arm64: gic-v5: Sanitize
 ID_AA64PFR2_EL1.GCIE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
43. **[01-08 10:25]** Re: [PATCH v2 07/36] KVM: arm64: gic: Introduce interrupt type
 helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
44. **[01-08 10:26]** Re: [PATCH v2 08/36] KVM: arm64: Introduce kvm_call_hyp_nvhe_res()
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
45. **[01-08 10:36]** Re: [PATCH v2 11/36] KVM: arm64: gic-v5: Support GICv5 FGTs & FGUs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
46. **[01-08 13:39]** Re: [PATCH v2 13/36] KVM: arm64: gic: Set vgic_model before initing
 private IRQs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
47. **[01-08 13:40]** Re: [PATCH v2 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
48. **[01-08 14:43]** Re: [PATCH v2 18/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
49. **[01-08 16:10]** Re: [PATCH v2 19/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Joey Gouly <joey.gouly@arm.com>
50. **[01-08 16:21]** Re: [PATCH v2 19/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
51. **[01-08 16:23]** Re: [PATCH v2 19/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
52. **[01-08 16:51]** Re: [PATCH v2 21/36] KVM: arm64: gic-v5: Finalize GICv5 PPIs and
 generate mask
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
53. **[01-08 16:52]** Re: [PATCH v2 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put
 and save/restore
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
54. **[01-08 16:52]** Re: [PATCH v2 01/36] KVM: arm64: Account for RES1 bits in
 DECLARE_FEAT_MAP() and co
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
55. **[01-08 16:53]** Re: [PATCH v2 23/36] KVM: arm64: gic-v5: Support GICv5 interrupts
 with KVM_IRQ_LINE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
56. **[01-08 16:55]** Re: [PATCH v2 24/36] KVM: arm64: gic-v5: Create, init vgic_v5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
57. **[01-08 16:57]** Re: [PATCH v2 19/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
58. **[01-09 15:00]** Re: [PATCH v2 33/36] KVM: arm64: gic-v5: Probe for GICv5 device
   - 发件人: Joey Gouly <joey.gouly@arm.com>
59. **[01-09 16:56]** Re: [PATCH v2 26/36] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
60. **[01-09 16:57]** Re: [PATCH v2 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
61. **[01-09 16:59]** Re: [PATCH v2 22/36] KVM: arm64: gic-v5: Trap and mask guest PPI
 register accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
62. **[01-09 17:00]** Re: [PATCH v2 36/36] KVM: arm64: gic-v5: Communicate
 userspace-drivable PPIs via a UAPI
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 3: [PATCH 00/30] KVM: arm64: Add support for protected guest memory with pKVM

**📧 邮件数**: 61 | **👥 参与者**: 5 | **📅 开始时间**: Mon,  5 Jan 2026 15:49:08 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上实现受保护的虚拟机（pVM）支持的补丁系列，主要集中在 pKVM 的功能扩展和实现细节。

1. **原始补丁/问题内容**：
   本次补丁系列的核心是为 KVM 添加对受保护的来宾内存的支持，允许通过 pKVM 进行内存捐赠和回收。补丁系列包括多个功能模块，如内存捐赠、处理不当主机访问受保护内存的机制、以及新的超调用（hypercall）接口等。

2. **之前讨论要点**：
   之前的讨论主要集中在如何将 pVM 功能逐步引入主线，尤其是如何处理与用户空间的交互和测试。同时，开发者们对如何在不影响现有功能的情况下逐步实现这些功能表示关注。

3. **本周的新讨论、进展或结论**：
   本周的讨论包括多个补丁的提交和审查，主要内容包括：
   - 引入了新的超调用接口以支持 pVM 的内存共享和取消共享功能。
   - 增加了对受保护虚拟机的创建支持，允许用户空间通过 KVM_CREATE_VM ioctl() 请求创建受保护的虚拟机。
   - 讨论了如何在处理内存访问错误时返回适当的错误代码，以及如何在不同情况下处理 pVM 的内存回收。
   - 还对现有的自测功能进行了扩展，以覆盖新的内存捐赠和回收场景。

整体来看，本周的讨论和补丁提交标志着 pKVM 功能的逐步完善，开发者们对如何确保安全性和功能完整性进行了深入探讨。

#### 📝 邮件列表

1. **[01-05 15:49]** [PATCH 00/30] KVM: arm64: Add support for protected guest memory with pKVM
   - 发件人: Will Deacon <will@kernel.org>
2. **[01-05 15:49]** [PATCH 01/30] KVM: arm64: Invert KVM_PGTABLE_WALK_HANDLE_FAULT to fix pKVM walkers
   - 发件人: Will Deacon <will@kernel.org>
3. **[01-05 15:49]** [PATCH 02/30] KVM: arm64: Remove redundant 'pgt' pointer checks from MMU notifiers
   - 发件人: Will Deacon <will@kernel.org>
4. **[01-05 15:49]** [PATCH 03/30] KVM: arm64: Rename __pkvm_pgtable_stage2_unmap()
   - 发件人: Will Deacon <will@kernel.org>
5. **[01-05 15:49]** [PATCH 04/30] KVM: arm64: Don't advertise unsupported features for protected guests
   - 发件人: Will Deacon <will@kernel.org>
6. **[01-05 15:49]** [PATCH 05/30] KVM: arm64: Expose self-hosted debug regs as RAZ/WI for protected guests
   - 发件人: Will Deacon <will@kernel.org>
7. **[01-05 15:49]** [PATCH 06/30] KVM: arm64: Remove pointless is_protected_kvm_enabled() checks from hyp
   - 发件人: Will Deacon <will@kernel.org>
8. **[01-05 15:49]** [PATCH 07/30] KVM: arm64: Ignore MMU notifier callbacks for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
9. **[01-05 15:49]** [PATCH 08/30] KVM: arm64: Prevent unsupported memslot operations on protected VMs
   - 发件人: Will Deacon <will@kernel.org>
10. **[01-05 15:49]** [PATCH 09/30] KVM: arm64: Split teardown hypercall into two phases
   - 发件人: Will Deacon <will@kernel.org>
11. **[01-05 15:49]** [PATCH 10/30] KVM: arm64: Introduce __pkvm_host_donate_guest()
   - 发件人: Will Deacon <will@kernel.org>
12. **[01-05 15:49]** [PATCH 11/30] KVM: arm64: Hook up donation hypercall to pkvm_pgtable_stage2_map()
   - 发件人: Will Deacon <will@kernel.org>
13. **[01-05 15:49]** [PATCH 12/30] KVM: arm64: Handle aborts from protected VMs
   - 发件人: Will Deacon <will@kernel.org>
14. **[01-05 15:49]** [PATCH 13/30] KVM: arm64: Introduce __pkvm_reclaim_dying_guest_page()
   - 发件人: Will Deacon <will@kernel.org>
15. **[01-05 15:49]** [PATCH 14/30] KVM: arm64: Hook up reclaim hypercall to pkvm_pgtable_stage2_destroy()
   - 发件人: Will Deacon <will@kernel.org>
16. **[01-05 15:49]** [PATCH 15/30] KVM: arm64: Refactor enter_exception64()
   - 发件人: Will Deacon <will@kernel.org>
17. **[01-05 15:49]** [PATCH 16/30] KVM: arm64: Inject SIGSEGV on illegal accesses
   - 发件人: Will Deacon <will@kernel.org>
18. **[01-05 15:49]** [PATCH 17/30] KVM: arm64: Generalise kvm_pgtable_stage2_set_owner()
   - 发件人: Will Deacon <will@kernel.org>
19. **[01-05 15:49]** [PATCH 18/30] KVM: arm64: Introduce host_stage2_set_owner_metadata_locked()
   - 发件人: Will Deacon <will@kernel.org>
20. **[01-05 15:49]** [PATCH 19/30] KVM: arm64: Annotate guest donations with handle and gfn in host stage-2
   - 发件人: Will Deacon <will@kernel.org>
21. **[01-05 15:49]** [PATCH 20/30] KVM: arm64: Introduce hypercall to force reclaim of a protected page
   - 发件人: Will Deacon <will@kernel.org>
22. **[01-05 15:49]** [PATCH 21/30] KVM: arm64: Reclaim faulting page from pKVM in spurious fault handler
   - 发件人: Will Deacon <will@kernel.org>
23. **[01-05 15:49]** [PATCH 22/30] KVM: arm64: Return -EFAULT from VCPU_RUN on access to a poisoned pte
   - 发件人: Will Deacon <will@kernel.org>
24. **[01-05 15:49]** [PATCH 23/30] KVM: arm64: Add hvc handler at EL2 for hypercalls from protected VMs
   - 发件人: Will Deacon <will@kernel.org>
25. **[01-05 15:49]** [PATCH 24/30] KVM: arm64: Implement the MEM_SHARE hypercall for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
26. **[01-05 15:49]** [PATCH 25/30] KVM: arm64: Implement the MEM_UNSHARE hypercall for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
27. **[01-05 15:49]** [PATCH 26/30] KVM: arm64: Allow userspace to create protected VMs when pKVM is enabled
   - 发件人: Will Deacon <will@kernel.org>
28. **[01-05 15:49]** [PATCH 27/30] KVM: arm64: Add some initial documentation for pKVM
   - 发件人: Will Deacon <will@kernel.org>
29. **[01-05 15:49]** [PATCH 28/30] KVM: arm64: Extend pKVM page ownership selftests to cover guest donation
   - 发件人: Will Deacon <will@kernel.org>
30. **[01-05 15:49]** [PATCH 29/30] KVM: arm64: Register 'selftest_vm' in the VM table
   - 发件人: Will Deacon <will@kernel.org>
31. **[01-05 15:49]** [PATCH 30/30] KVM: arm64: Extend pKVM page ownership selftests to cover forced reclaim
   - 发件人: Will Deacon <will@kernel.org>
32. **[01-06 14:32]** Re: [PATCH 02/30] KVM: arm64: Remove redundant 'pgt' pointer checks
 from MMU notifiers
   - 发件人: Quentin Perret <qperret@google.com>
33. **[01-06 14:33]** Re: [PATCH 01/30] KVM: arm64: Invert KVM_PGTABLE_WALK_HANDLE_FAULT
 to fix pKVM walkers
   - 发件人: Quentin Perret <qperret@google.com>
34. **[01-06 14:40]** Re: [PATCH 06/30] KVM: arm64: Remove pointless
 is_protected_kvm_enabled() checks from hyp
   - 发件人: Quentin Perret <qperret@google.com>
35. **[01-06 14:48]** Re: [PATCH 10/30] KVM: arm64: Introduce __pkvm_host_donate_guest()
   - 发件人: Quentin Perret <qperret@google.com>
36. **[01-06 14:59]** Re: [PATCH 14/30] KVM: arm64: Hook up reclaim hypercall to
 pkvm_pgtable_stage2_destroy()
   - 发件人: Quentin Perret <qperret@google.com>
37. **[01-06 15:20]** Re: [PATCH 17/30] KVM: arm64: Generalise
 kvm_pgtable_stage2_set_owner()
   - 发件人: Quentin Perret <qperret@google.com>
38. **[01-06 15:44]** Re: [PATCH 20/30] KVM: arm64: Introduce hypercall to force reclaim
 of a protected page
   - 发件人: Quentin Perret <qperret@google.com>
39. **[01-06 15:45]** Re: [PATCH 24/30] KVM: arm64: Implement the MEM_SHARE hypercall for
 protected VMs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
40. **[01-06 15:50]** Re: [PATCH 25/30] KVM: arm64: Implement the MEM_UNSHARE hypercall
 for protected VMs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
41. **[01-06 15:52]** Re: [PATCH 23/30] KVM: arm64: Add hvc handler at EL2 for hypercalls
 from protected VMs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
42. **[01-06 15:54]** Re: [PATCH 22/30] KVM: arm64: Return -EFAULT from VCPU_RUN on access
 to a poisoned pte
   - 发件人: Quentin Perret <qperret@google.com>
43. **[01-06 15:59]** Re: [PATCH 27/30] KVM: arm64: Add some initial documentation for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
44. **[01-06 16:01]** Re: [PATCH 19/30] KVM: arm64: Annotate guest donations with handle
 and gfn in host stage-2
   - 发件人: Fuad Tabba <tabba@google.com>
45. **[01-06 16:26]** Re: [PATCH 13/30] KVM: arm64: Introduce
 __pkvm_reclaim_dying_guest_page()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
46. **[01-09 14:23]** Re: [PATCH 06/30] KVM: arm64: Remove pointless
 is_protected_kvm_enabled() checks from hyp
   - 发件人: Will Deacon <will@kernel.org>
47. **[01-09 14:30]** Re: [PATCH 10/30] KVM: arm64: Introduce __pkvm_host_donate_guest()
   - 发件人: Will Deacon <will@kernel.org>
48. **[01-09 14:31]** Re: [PATCH 02/30] KVM: arm64: Remove redundant 'pgt' pointer checks
 from MMU notifiers
   - 发件人: Will Deacon <will@kernel.org>
49. **[01-09 14:35]** Re: [PATCH 14/30] KVM: arm64: Hook up reclaim hypercall to
 pkvm_pgtable_stage2_destroy()
   - 发件人: Will Deacon <will@kernel.org>
50. **[01-09 14:42]** Re: [PATCH 19/30] KVM: arm64: Annotate guest donations with handle
 and gfn in host stage-2
   - 发件人: Will Deacon <will@kernel.org>
51. **[01-09 14:57]** Re: [PATCH 22/30] KVM: arm64: Return -EFAULT from VCPU_RUN on access
 to a poisoned pte
   - 发件人: Will Deacon <will@kernel.org>
52. **[01-09 14:57]** Re: [PATCH 14/30] KVM: arm64: Hook up reclaim hypercall to
 pkvm_pgtable_stage2_destroy()
   - 发件人: Quentin Perret <qperret@google.com>
53. **[01-09 15:01]** Re: [PATCH 24/30] KVM: arm64: Implement the MEM_SHARE hypercall for
 protected VMs
   - 发件人: Will Deacon <will@kernel.org>
54. **[01-09 15:04]** Re: [PATCH 27/30] KVM: arm64: Add some initial documentation for pKVM
   - 发件人: Will Deacon <will@kernel.org>
55. **[01-09 15:10]** Re: [PATCH 10/30] KVM: arm64: Introduce __pkvm_host_donate_guest()
   - 发件人: Quentin Perret <qperret@google.com>
56. **[01-09 15:29]** Re: [PATCH 22/30] KVM: arm64: Return -EFAULT from VCPU_RUN on access
 to a poisoned pte
   - 发件人: Quentin Perret <qperret@google.com>
57. **[01-09 17:31]** Re: [PATCH 02/30] KVM: arm64: Remove redundant 'pgt' pointer checks
 from MMU notifiers
   - 发件人: Will Deacon <will@kernel.org>
58. **[01-09 17:35]** Re: [PATCH 22/30] KVM: arm64: Return -EFAULT from VCPU_RUN on access
 to a poisoned pte
   - 发件人: Will Deacon <will@kernel.org>
59. **[01-09 17:47]** Re: [PATCH 20/30] KVM: arm64: Introduce hypercall to force reclaim
 of a protected page
   - 发件人: Will Deacon <will@kernel.org>
60. **[01-09 18:46]** Re: [PATCH 17/30] KVM: arm64: Generalise
 kvm_pgtable_stage2_set_owner()
   - 发件人: Will Deacon <will@kernel.org>
61. **[01-10 02:22]** Re: (subset) [PATCH 01/30] KVM: arm64: Invert KVM_PGTABLE_WALK_HANDLE_FAULT to fix pKVM walkers
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 4: [PATCH v9 00/30] KVM: arm64: Implement support for SME

**📧 邮件数**: 47 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 23 Dec 2025 01:20:54 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中实现对 ARM64 的可扩展矩阵扩展（SME）支持的补丁系列。

1. **原始补丁/问题内容**：Mark Brown 提出了一个包含 30 个补丁的系列，旨在为 ARM64 的 KVM 实现 SME 支持。补丁涉及用户空间 ABI、SVE 和 SME 的寄存器访问、动态配置等多个方面。

2. **之前讨论要点**：历史讨论中，参与者关注了补丁的用户空间 ABI 设计、SVE 和 SME 的寄存器访问方式，以及如何在 KVM 中动态管理这些寄存器的状态。补丁系列的初步反馈集中在对现有功能的兼容性和实现细节的讨论。

3. **本周的新讨论与进展**：本周的讨论主要集中在对补丁的细节审查上。Marc Zyngier 和 Fuad Tabba 提出了对补丁的具体建议，包括对某些宏的命名、代码的可读性以及对寄存器状态的管理等。Fuad Tabba 对多个补丁进行了审核并给予了“Reviewed-by”的标记，表明这些补丁在技术上是可接受的。此外，讨论中还提到了一些潜在的问题和改进建议，例如对寄存器值的处理和上下文信息的提供。

总体来看，本周的讨论进一步推动了补丁的审查进程，参与者积极提出改进意见，为最终的补丁集成做准备。

#### 📝 邮件列表

1. **[12-23 01:20]** [PATCH v9 00/30] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[12-23 01:20]** [PATCH v9 01/30] arm64/sysreg: Update SMIDR_EL1 to DDI0601 2025-06
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[12-23 01:20]** [PATCH v9 02/30] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[12-23 01:20]** [PATCH v9 03/30] arm64/fpsimd: Decide to save ZT0 and streaming
 mode FFR at bind time
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[12-23 01:20]** [PATCH v9 04/30] arm64/fpsimd: Check enable bit for FA64 when
 saving EFI state
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[12-23 01:20]** [PATCH v9 05/30] arm64/fpsimd: Determine maximum virtualisable SME
 vector length
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[12-23 01:21]** [PATCH v9 06/30] KVM: arm64: Pay attention to FFR parameter in SVE
 save and load
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[12-23 01:21]** [PATCH v9 07/30] KVM: arm64: Pull ctxt_has_ helpers to start of
 sysreg-sr.h
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[12-23 01:21]** [PATCH v9 08/30] KVM: arm64: Move SVE state access macros after
 feature test macros
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[12-23 01:21]** [PATCH v9 09/30] KVM: arm64: Rename SVE finalization constants to
 be more general
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[12-23 01:21]** [PATCH v9 10/30] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[12-23 01:21]** [PATCH v9 11/30] KVM: arm64: Define internal features for SME
   - 发件人: Mark Brown <broonie@kernel.org>
13. **[12-23 01:21]** [PATCH v9 12/30] KVM: arm64: Rename sve_state_reg_region
   - 发件人: Mark Brown <broonie@kernel.org>
14. **[12-23 01:21]** [PATCH v9 13/30] KVM: arm64: Store vector lengths in an array
   - 发件人: Mark Brown <broonie@kernel.org>
15. **[12-23 01:21]** [PATCH v9 14/30] KVM: arm64: Implement SME vector length
 configuration
   - 发件人: Mark Brown <broonie@kernel.org>
16. **[12-23 01:21]** [PATCH v9 15/30] KVM: arm64: Support SME control registers
   - 发件人: Mark Brown <broonie@kernel.org>
17. **[12-23 01:21]** [PATCH v9 16/30] KVM: arm64: Support TPIDR2_EL0
   - 发件人: Mark Brown <broonie@kernel.org>
18. **[12-23 01:21]** [PATCH v9 17/30] KVM: arm64: Support SME identification registers
 for guests
   - 发件人: Mark Brown <broonie@kernel.org>
19. **[01-07 13:45]** Re: [PATCH v9 21/30] KVM: arm64: Initialise hyp_nr_cpus for nVHE hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[01-07 14:23]** Re: [PATCH v9 25/30] KVM: arm64: Sync boot clock with the nVHE/pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[01-07 14:37]** Re: [PATCH v9 28/30] KVM: arm64: Add hyp_enter/hyp_exit events to nVHE/pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[01-07 15:40]** Re: [PATCH v9 29/30] KVM: arm64: Add selftest event support to nVHE/pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[01-07 16:00]** Re: [PATCH v9 00/30] Tracefs support for pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
24. **[01-07 11:36]** Re: [PATCH v9 28/30] KVM: arm64: Add hyp_enter/hyp_exit events to
 nVHE/pKVM hyp
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
25. **[01-07 11:59]** Re: [PATCH v9 00/30] Tracefs support for pKVM
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
26. **[01-07 19:24]** Re: [PATCH v9 01/30] arm64/sysreg: Update SMIDR_EL1 to DDI0601 2025-06
   - 发件人: Fuad Tabba <tabba@google.com>
27. **[01-07 19:25]** Re: [PATCH v9 02/30] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Fuad Tabba <tabba@google.com>
28. **[01-07 19:25]** Re: [PATCH v9 03/30] arm64/fpsimd: Decide to save ZT0 and streaming
 mode FFR at bind time
   - 发件人: Fuad Tabba <tabba@google.com>
29. **[01-07 19:25]** Re: [PATCH v9 04/30] arm64/fpsimd: Check enable bit for FA64 when
 saving EFI state
   - 发件人: Fuad Tabba <tabba@google.com>
30. **[01-07 19:25]** Re: [PATCH v9 05/30] arm64/fpsimd: Determine maximum virtualisable
 SME vector length
   - 发件人: Fuad Tabba <tabba@google.com>
31. **[01-08 11:54]** Re: [PATCH v9 02/30] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Mark Brown <broonie@kernel.org>
32. **[01-08 14:09]** Re: [PATCH v9 02/30] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Fuad Tabba <tabba@google.com>
33. **[01-08 14:09]** Re: [PATCH v9 06/30] KVM: arm64: Pay attention to FFR parameter in
 SVE save and load
   - 发件人: Fuad Tabba <tabba@google.com>
34. **[01-08 14:09]** Re: [PATCH v9 07/30] KVM: arm64: Pull ctxt_has_ helpers to start of sysreg-sr.h
   - 发件人: Fuad Tabba <tabba@google.com>
35. **[01-08 14:09]** Re: [PATCH v9 08/30] KVM: arm64: Move SVE state access macros after
 feature test macros
   - 发件人: Fuad Tabba <tabba@google.com>
36. **[01-08 14:09]** Re: [PATCH v9 09/30] KVM: arm64: Rename SVE finalization constants to
 be more general
   - 发件人: Fuad Tabba <tabba@google.com>
37. **[01-08 14:10]** Re: [PATCH v9 10/30] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Fuad Tabba <tabba@google.com>
38. **[01-08 15:57]** Re: [PATCH v9 02/30] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Mark Brown <broonie@kernel.org>
39. **[01-08 16:19]** Re: [PATCH v9 02/30] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Fuad Tabba <tabba@google.com>
40. **[01-08 16:42]** Re: [PATCH v9 02/30] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Mark Brown <broonie@kernel.org>
41. **[01-09 15:55]** Re: [PATCH v9 11/30] KVM: arm64: Define internal features for SME
   - 发件人: Fuad Tabba <tabba@google.com>
42. **[01-09 15:55]** Re: [PATCH v9 12/30] KVM: arm64: Rename sve_state_reg_region
   - 发件人: Fuad Tabba <tabba@google.com>
43. **[01-09 15:55]** Re: [PATCH v9 13/30] KVM: arm64: Store vector lengths in an array
   - 发件人: Fuad Tabba <tabba@google.com>
44. **[01-09 15:59]** Re: [PATCH v9 14/30] KVM: arm64: Implement SME vector length configuration
   - 发件人: Fuad Tabba <tabba@google.com>
45. **[01-09 16:31]** Re: [PATCH v9 15/30] KVM: arm64: Support SME control registers
   - 发件人: Fuad Tabba <tabba@google.com>
46. **[01-09 16:57]** Re: [PATCH v9 16/30] KVM: arm64: Support TPIDR2_EL0
   - 发件人: Fuad Tabba <tabba@google.com>
47. **[01-09 18:01]** Re: [PATCH v9 17/30] KVM: arm64: Support SME identification registers
 for guests
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 5: [PATCH v3 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support

**📧 邮件数**: 37 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 9 Jan 2026 17:04:39 +0000

#### 🤖 AI 总结

本邮件讨论的主题是引入对 KVM（Kernel-based Virtual Machine）中 GICv5（Generic Interrupt Controller v5）的支持，主要集中在对 PPI（Private Peripheral Interrupts）的处理和相关功能的实现。

1. **原始 Patch/问题内容**：
   - 本次讨论的核心是一个包含 36 个补丁的系列，旨在为 KVM 的 arm64 架构引入对 GICv5 的支持，特别是 PPI 的处理。补丁系列的主要目标是实现 GICv5 的基本功能，包括 PPI 的保存、恢复和直接注入等。

2. **之前讨论要点**：
   - 在之前的讨论中，参与者们探讨了 GICv5 的架构特性及其与 GICv3 的不同之处，特别是在中断管理和状态同步方面。GICv5 允许通过硬件直接管理 PPI 的状态，减少了对软件中断队列的依赖。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论中，补丁系列逐步完善了 GICv5 的功能，包括实现 PPI 的直接注入、状态检查和优先级管理。具体补丁包括：
     - 增加了对 GICv5 设备的探测和初始化支持。
     - 引入了用户空间驱动的 PPI 掩码，确保只有实现的 PPI 可以被用户空间驱动。
     - 实现了对 ICC_PPI_ENABLERx_EL1 寄存器的写入监控，防止未实现的 PPI 被启用。
     - 提供了自测功能，确保 GICv5 的基本操作正常。

总的来说，本周的讨论和补丁实现了 GICv5 的基本支持，为未来的功能扩展奠定了基础。

#### 📝 邮件列表

1. **[01-09 17:04]** [PATCH v3 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[01-09 17:04]** [PATCH v3 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use generated
 ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[01-09 17:04]** [PATCH v3 01/36] KVM: arm64: Account for RES1 bits in
 DECLARE_FEAT_MAP() and co
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[01-09 17:04]** [PATCH v3 03/36] arm64/sysreg: Drop ICH_HFGRTR_EL2.ICC_HAPR_EL1 and
 make RES1
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[01-09 17:04]** [PATCH v3 04/36] arm64/sysreg: Add remaining GICv5 ICC_ & ICH_
 sysregs for KVM support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[01-09 17:04]** [PATCH v3 06/36] KVM: arm64: gic: Set vgic_model before initing
 private IRQs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[01-09 17:04]** [PATCH v3 05/36] arm64/sysreg: Add GICR CDNMIA encoding
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[01-09 17:04]** [PATCH v3 08/36] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
9. **[01-09 17:04]** [PATCH v3 09/36] KVM: arm64: gic-v5: Add Arm copyright header
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[01-09 17:04]** [PATCH v3 07/36] KVM: arm64: gic-v5: Add ARM_VGIC_V5 device to KVM
 headers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
11. **[01-09 17:04]** [PATCH v3 12/36] KVM: arm64: gic-v5: Support GICv5 FGTs & FGUs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[01-09 17:04]** [PATCH v3 10/36] KVM: arm64: gic-v5: Detect implemented PPIs on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[01-09 17:04]** [PATCH v3 11/36] KVM: arm64: gic-v5: Sanitize ID_AA64PFR2_EL1.GCIE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[01-09 17:04]** [PATCH v3 14/36] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp
 interface
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[01-09 17:04]** [PATCH v3 13/36] KVM: arm64: gic-v5: Add emulation for
 ICC_IAFFIDR_EL1 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
16. **[01-09 17:04]** [PATCH v3 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[01-09 17:04]** [PATCH v3 18/36] KVM: arm64: gic: Introduce queue_irq_unlock and
 set_pending_state to irq_ops
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
18. **[01-09 17:04]** [PATCH v3 17/36] KVM: arm64: gic-v5: Finalize GICv5 PPIs and generate
 mask
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
19. **[01-09 17:04]** [PATCH v3 16/36] KVM: arm64: gic-v5: Implement direct injection of
 PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
20. **[01-09 17:04]** [PATCH v3 19/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
21. **[01-09 17:04]** [PATCH v3 20/36] KVM: arm64: gic-v5: Init Private IRQs (PPIs) for
 GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
22. **[01-09 17:04]** [PATCH v3 23/36] KVM: arm64: gic-v5: Support GICv5 interrupts with
 KVM_IRQ_LINE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
23. **[01-09 17:04]** [PATCH v3 22/36] KVM: arm64: gic-v5: Trap and mask guest
 ICC_PPI_ENABLERx_EL1 writes
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
24. **[01-09 17:04]** [PATCH v3 21/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
25. **[01-09 17:04]** [PATCH v3 26/36] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
26. **[01-09 17:04]** [PATCH v3 27/36] KVM: arm64: gic-v5: Mandate architected PPI for PMU
 emulation on GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
27. **[01-09 17:04]** [PATCH v3 24/36] KVM: arm64: gic-v5: Create, init vgic_v5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
28. **[01-09 17:04]** [PATCH v3 25/36] KVM: arm64: gic-v5: Reset vcpu state
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
29. **[01-09 17:04]** [PATCH v3 30/36] KVM: arm64: gic-v5: Introduce kvm_arm_vgic_v5_ops
 and register them
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
30. **[01-09 17:04]** [PATCH v3 29/36] KVM: arm64: gic-v5: Hide FEAT_GCIE from NV GICv5
 guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
31. **[01-09 17:04]** [PATCH v3 28/36] KVM: arm64: gic: Hide GICv5 for protected guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
32. **[01-09 17:04]** [PATCH v3 34/36] Documentation: KVM: Introduce documentation for
 VGICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
33. **[01-09 17:04]** [PATCH v3 33/36] KVM: arm64: gic-v5: Probe for GICv5 device
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
34. **[01-09 17:04]** [PATCH v3 31/36] KVM: arm64: gic-v5: Set ICH_VCTLR_EL2.En on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
35. **[01-09 17:04]** [PATCH v3 32/36] irqchip/gic-v5: Check if impl is virt capable
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
36. **[01-09 17:04]** [PATCH v3 35/36] KVM: arm64: selftests: Introduce a minimal GICv5 PPI
 selftest
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
37. **[01-09 17:04]** [PATCH v3 36/36] KVM: arm64: gic-v5: Communicate userspace-driveable
 PPIs via a UAPI
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 6: [PATCH v4 0/5] KVM: selftests: arm64: Improve diagnostics from
 set_id_regs

**📧 邮件数**: 14 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 06 Jan 2026 16:35:40 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 自测试的补丁系列，主要集中在改进 ARM64 架构下的 `set_id_regs` 测试的诊断信息。补丁分为五个部分，旨在提高测试的可读性和准确性。

1. **原始补丁内容**：补丁的核心是改进 `set_id_regs` 测试中的错误报告机制，特别是在执行寄存器读取和重置值保持测试时，原有的错误报告缺乏细节，导致无法明确识别出问题寄存器。补丁通过为每个寄存器单独报告测试结果来解决这一问题。

2. **之前讨论要点**：在历史讨论中，参与者指出了现有测试中使用立即致命断言的问题，这使得测试失败时难以确定具体的错误。补丁更新了这些断言，采用标准的 kselftest 报告形式，使得测试结果更易于理解。

3. **本周的新讨论与进展**：本周的讨论中，Mark Brown 提出了补丁的具体实现细节，包括对寄存器名称的处理和对 32 位 ID 寄存器的跳过逻辑。Ben Horgan 对某些检查的合理性提出了疑问，讨论了在 AArch64 系统中如何处理 ID 寄存器的可访问性。此外，Fuad Tabba 提出了与内存对齐和 MMU 配置相关的补丁，进一步增强了 KVM 自测试的稳定性和准确性。

总体而言，该系列补丁通过改进测试报告和修复潜在的错误，提升了 KVM 在 ARM64 架构下的自测试质量。

#### 📝 邮件列表

1. **[01-06 16:35]** [PATCH v4 0/5] KVM: selftests: arm64: Improve diagnostics from
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[01-06 16:35]** [PATCH v4 1/5] KVM: selftests: arm64: Report set_id_reg reads of
 test registers as tests
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[01-06 16:35]** [PATCH v4 2/5] KVM: selftests: arm64: Report register reset tests
 individually
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[01-06 16:35]** [PATCH v4 3/5] KVM: selftests: arm64: Make set_id_regs bitfield
 validatity checks non-fatal
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[01-06 16:35]** [PATCH v4 4/5] KVM: selftests: arm64: Skip all 32 bit IDs when
 set_id_regs is aarch64 only
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[01-06 16:35]** [PATCH v4 5/5] KVM: selftests: arm64: Use is_aarch32_id_reg() in
 test_vm_ftr_id_regs()
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[01-07 09:54]** Re: [PATCH v4 4/5] KVM: selftests: arm64: Skip all 32 bit IDs when
 set_id_regs is aarch64 only
   - 发件人: Ben Horgan <ben.horgan@arm.com>
8. **[01-07 11:44]** Re: [PATCH v4 4/5] KVM: selftests: arm64: Skip all 32 bit IDs when
 set_id_regs is aarch64 only
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[01-09 08:22]** [PATCH v4 0/5] KVM: selftests: Alignment fixes and arm64 MMU cleanup
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[01-09 08:22]** [PATCH v4 1/5] KVM: arm64: selftests: Disable unused TTBR1_EL1 translations
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[01-09 08:22]** [PATCH v4 2/5] KVM: arm64: selftests: Fix incorrect rounding in page_align()
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[01-09 08:22]** [PATCH v4 3/5] KVM: riscv: selftests: Fix incorrect rounding in page_align()
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[01-09 08:22]** [PATCH v4 4/5] KVM: selftests: Move page_align() to shared header
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[01-09 08:22]** [PATCH v4 5/5] KVM: selftests: Fix typos and stale comments in kvm_util
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 7: [PATCH 0/3] KVM: arm64: Trivial FPSIMD cleanups

**📧 邮件数**: 14 | **👥 参与者**: 4 | **📅 开始时间**: Tue,  6 Jan 2026 17:37:04 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 FPSIMD（Floating Point SIMD）相关的清理补丁，共包含三部分补丁。

1. **原始补丁内容**：
   - 该补丁系列旨在对 FPSIMD/SVE/SME 重构过程中遗留的一些小问题进行清理。具体包括：
     - 修正 fpsimd_lazy_switch_to_host() 函数中的注释错误。
     - 重新排列 KVM_HOST_DATA_FLAG_* 索引以消除空隙。
     - 移除在写入 FPEXC32_EL2 后不必要的 ISB（指令同步屏障）。

2. **之前的讨论要点**：
   - 在之前的讨论中，Mark Rutland 提到这些补丁是为了清理去年 FPSIMD/SVE/SME 重构过程中遗留的细节，确保代码的整洁性和可维护性。

3. **本周的新讨论与进展**：
   - 本周的讨论中，Mark Rutland 提交了补丁并获得了多位参与者的测试和审核反馈，包括 Fuad Tabba 和 Mark Brown，均表示已测试并审核通过。Marc Zyngier 最终确认将这些补丁应用到下一个版本中，表明补丁已被接受并将进入主线代码。

总体来看，本周的讨论集中在对 FPSIMD 相关代码的小幅清理上，补丁经过测试和审核后顺利通过，标志着该系列补丁的成功提交。

#### 📝 邮件列表

1. **[01-06 17:37]** [PATCH 0/3] KVM: arm64: Trivial FPSIMD cleanups
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[01-06 17:37]** [PATCH 1/3] KVM: arm64: Fix comment in fpsimd_lazy_switch_to_host()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
3. **[01-06 17:37]** [PATCH 2/3] KVM: arm64: Shuffle KVM_HOST_DATA_FLAG_* indices
   - 发件人: Mark Rutland <mark.rutland@arm.com>
4. **[01-06 17:37]** [PATCH 3/3] KVM: arm64: Remove ISB after writing FPEXC32_EL2
   - 发件人: Mark Rutland <mark.rutland@arm.com>
5. **[01-07 10:48]** Re: [PATCH 1/3] KVM: arm64: Fix comment in fpsimd_lazy_switch_to_host()
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[01-07 10:49]** Re: [PATCH 2/3] KVM: arm64: Shuffle KVM_HOST_DATA_FLAG_* indices
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[01-07 10:49]** Re: [PATCH 3/3] KVM: arm64: Remove ISB after writing FPEXC32_EL2
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[01-07 11:23]** Re: [PATCH 2/3] KVM: arm64: Shuffle KVM_HOST_DATA_FLAG_* indices
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[01-07 11:59]** Re: [PATCH 0/3] KVM: arm64: Trivial FPSIMD cleanups
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[01-07 11:59]** Re: [PATCH 3/3] KVM: arm64: Remove ISB after writing FPEXC32_EL2
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[01-07 18:06]** [PATCH 0/3] arm64: Unconditionally compile LSE/PAN/EPAN support
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[01-07 18:06]** [PATCH 1/3] arm64: Unconditionally enable LSE support
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[01-07 18:07]** [PATCH 2/3] arm64: Unconditionally enable PAN support
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[01-07 18:07]** [PATCH 3/3] arm64: Unconditionally enable EPAN support
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v4 00/21] KVM: selftests: Add Nested NPT support

**📧 邮件数**: 12 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 30 Dec 2025 15:01:29 -0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM 的自测试，特别是新增对嵌套 NPT（Nested Page Table）支持的补丁。历史讨论中，Yosry 提出了一个包含 21 个补丁的系列，旨在增强 KVM 的自测试功能，特别是扩展 vmx_dirty_log_test 和 kvm_dirty_log_test，以支持嵌套 SVM。Sean Christopherson 对某些补丁的稳定性表示担忧，尤其是涉及到内存压力下的 READ 故障处理。

在本周的新讨论中，Yosry 和 Sean 针对补丁的细节进行了深入交流。Yosry 提到在实现嵌套 NPT 时，测试仍然通过，且对代码的部分进行了调整，使其更清晰。此外，Sean 提出了一些关于变量命名和宏定义的建议，以提高代码的可读性和一致性。两位参与者在讨论中保持了良好的互动，针对代码的细节进行了多次修改和优化，确保补丁的质量和功能。

总体来看，本周的讨论主要集中在代码细节的完善和命名一致性上，推动了补丁的进一步发展。

#### 📝 邮件列表

1. **[12-30 15:01]** [PATCH v4 00/21] KVM: selftests: Add Nested NPT support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[12-30 15:01]** [PATCH v4 16/21] KVM: selftests: Add support for nested NPTs
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[12-30 15:01]** [PATCH v4 21/21] KVM: selftests: Test READ=>WRITE dirty logging
 behavior for shadow MMU
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[01-02 17:36]** Re: [PATCH v4 21/21] KVM: selftests: Test READ=>WRITE dirty logging
 behavior for shadow MMU
   - 发件人: Yosry Ahmed <yosry.ahmed@linux.dev>
5. **[01-07 23:12]** Re: [PATCH v4 16/21] KVM: selftests: Add support for nested NPTs
   - 发件人: Yosry Ahmed <yosry.ahmed@linux.dev>
6. **[01-08 08:32]** Re: [PATCH v4 21/21] KVM: selftests: Test READ=>WRITE dirty logging
 behavior for shadow MMU
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[01-08 18:01]** Re: [PATCH v4 21/21] KVM: selftests: Test READ=>WRITE dirty logging
 behavior for shadow MMU
   - 发件人: Yosry Ahmed <yosry.ahmed@linux.dev>
8. **[01-08 10:31]** Re: [PATCH v4 21/21] KVM: selftests: Test READ=>WRITE dirty logging
 behavior for shadow MMU
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[01-08 20:24]** Re: [PATCH v4 21/21] KVM: selftests: Test READ=>WRITE dirty logging
 behavior for shadow MMU
   - 发件人: Yosry Ahmed <yosry.ahmed@linux.dev>
10. **[01-08 20:26]** Re: [PATCH v4 21/21] KVM: selftests: Test READ=>WRITE dirty logging
 behavior for shadow MMU
   - 发件人: Yosry Ahmed <yosry.ahmed@linux.dev>
11. **[01-08 12:29]** Re: [PATCH v4 21/21] KVM: selftests: Test READ=>WRITE dirty logging
 behavior for shadow MMU
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[01-08 20:33]** Re: [PATCH v4 21/21] KVM: selftests: Test READ=>WRITE dirty logging
 behavior for shadow MMU
   - 发件人: Yosry Ahmed <yosry.ahmed@linux.dev>

---

### Thread 9: [PATCH v4 0/9] KVM: arm64: Add support for FEAT_IDST

**📧 邮件数**: 10 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  8 Jan 2026 17:32:24 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上添加对 FEAT_IDST 特性的支持。FEAT_IDST 是 ARMv8.4 中引入的一项功能，允许在未实现的情况下捕获 ID 寄存器的访问，涉及 GMID_EL1、CCSIDR2_EL1 和 SMIDR_EL1 三个寄存器。

在历史讨论中，Marc Zyngier 提出了多个版本的补丁（patch），逐步完善了对 FEAT_IDST 的支持，包括对寄存器的处理、异常注入机制的改进以及对 pKVM 的适配。补丁的演变中，增加了对 ID_AA64MMFR2_EL1.IDS 的描述、引入了新的辅助函数，并对代码结构进行了重组。

本周的新讨论中，Marc Zyngier 提交了补丁的第 4 版，详细介绍了如何处理这些寄存器的捕获和异常注入。补丁中实现了对 GMID_EL1 的特定处理，增加了通用的同步异常注入原语，并对 CSSIDR2_EL1 和 SMIDR_EL1 的处理进行了简化。此外，补丁还确保在缺少 MTE 的情况下强制捕获 GMID_EL1。最后，新增了自测代码，以验证 FEAT_IDST 的功能是否正常。

总体来看，本周的进展主要集中在完善对 FEAT_IDST 的实现和测试，确保在不同条件下的寄存器访问能够正确处理。

#### 📝 邮件列表

1. **[01-08 17:32]** [PATCH v4 0/9] KVM: arm64: Add support for FEAT_IDST
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-08 17:32]** [PATCH v4 1/9] arm64: Repaint ID_AA64MMFR2_EL1.IDS description
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-08 17:32]** [PATCH v4 2/9] KVM: arm64: Add trap routing for GMID_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[01-08 17:32]** [PATCH v4 3/9] KVM: arm64: Add a generic synchronous exception injection primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[01-08 17:32]** [PATCH v4 4/9] KVM: arm64: Handle FEAT_IDST for sysregs without specific handlers
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[01-08 17:32]** [PATCH v4 5/9] KVM: arm64: Handle CSSIDR2_EL1 and SMIDR_EL1 in a generic way
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[01-08 17:32]** [PATCH v4 6/9] KVM: arm64: Force trap of GMID_EL1 when the guest doesn't have MTE
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[01-08 17:32]** [PATCH v4 7/9] KVM: arm64: pkvm: Add a generic synchronous exception injection primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[01-08 17:32]** [PATCH v4 8/9] KVM: arm64: pkvm: Report optional ID register traps with a 0x18 syndrome
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[01-08 17:32]** [PATCH v4 9/9] KVM: arm64: selftests: Add a test for FEAT_IDST
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH v3 0/5] KVM: selftests: Alignment fixes and arm64 MMU cleanup

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  6 Jan 2026 09:24:20 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 自测的补丁系列，主要集中在内存对齐修复和 arm64 MMU 清理上。补丁的主要内容包括：

1. **原始补丁/问题**：补丁系列（[PATCH v3 0/5]）旨在修复 KVM 自测中的内存对齐错误，增强 arm64 MMU 配置，并修复一些文档问题。

2. **之前讨论要点**：补丁在 v2 版本中收集了审核意见，并基于 Linux 6.19-rc4 进行了重基。补丁的核心是确保未使用的 TTBR1 地址范围在自测中被禁用，以避免不确定行为，同时修复了 `page_align()` 函数的实现，确保其正确处理已对齐的地址。

3. **本周的新讨论与进展**：本周的讨论中，Fuad Tabba 提交了补丁的具体实现，包括对 arm64 和 riscv 的 `page_align()` 函数的修复，以及将其移动到共享头文件 `kvm_util.h` 中以消除代码重复。Sean Christopherson 提出建议，将函数命名为 `vm_page_align()` 以更清晰地表明其与虚拟机页面大小的关系，Fuad 表示同意并将进行修改。

整体来看，此次讨论聚焦于提高 KVM 自测的准确性和可维护性，确保在不同架构下的内存对齐逻辑一致。

#### 📝 邮件列表

1. **[01-06 09:24]** [PATCH v3 0/5] KVM: selftests: Alignment fixes and arm64 MMU cleanup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[01-06 09:24]** [PATCH v3 1/5] KVM: arm64: selftests: Disable unused TTBR1_EL1 translations
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[01-06 09:24]** [PATCH v3 2/5] KVM: arm64: selftests: Fix incorrect rounding in page_align()
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[01-06 09:24]** [PATCH v3 3/5] KVM: riscv: selftests: Fix incorrect rounding in page_align()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[01-06 09:24]** [PATCH v3 4/5] KVM: selftests: Move page_align() to shared header
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[01-06 09:24]** [PATCH v3 5/5] KVM: selftests: Fix typos and stale comments in kvm_util
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[01-06 11:46]** Re: [PATCH v3 4/5] KVM: selftests: Move page_align() to shared header
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[01-06 19:48]** Re: [PATCH v3 4/5] KVM: selftests: Move page_align() to shared header
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 11: [PATCH v3 3/4] KVM: selftests: arm64: Make set_id_regs bitfield
 validatity checks non-fatal

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 2 Jan 2026 14:45:04 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 的自测试（selftests）相关的补丁，特别是针对 arm64 架构的 `set_id_regs` 位域有效性检查的非致命化处理。

**原始补丁内容**：
补丁内容为将 `set_id_regs` 的位域有效性检查设为非致命，这样在测试过程中即使出现问题，测试也不会立即终止。

**之前讨论要点**：
在历史讨论中，Ben Horgan 对补丁表示认可，并提到之前的断言（asserts）为何被优先考虑并不明确。此外，另一封邮件中，Ben 质疑了在 `set_id_regs` 仅适用于 aarch64 时，跳过所有 32 位 ID 是否合理，认为可能会排除不必要的寄存器。

**本周新讨论及进展**：
本周的讨论中，Mark Brown 提出了关于 KVM 自测试框架与 kselftest 框架之间的兼容性问题，指出当前测试程序的设计存在混合使用两种测试风格的问题。Mark 还承认之前的测试设计不够合理，并表示会进行更新。Ben 对此表示赞同，认为这是一个合理的决定。此外，Oliver Upton 提到之前的补丁已被应用于修复中，进一步推动了讨论的进展。

整体来看，邮件讨论围绕着 KVM 自测试的有效性和设计合理性展开，参与者们积极交流并推动补丁的完善。

#### 📝 邮件列表

1. **[01-02 14:45]** Re: [PATCH v3 3/4] KVM: selftests: arm64: Make set_id_regs bitfield
 validatity checks non-fatal
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[01-02 14:50]** Re: [PATCH v3 4/4] KVM: selftests: arm64: Skip all 32 bit IDs when
 set_id_regs is aarch64 only
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[01-05 12:15]** Re: [PATCH v3 3/4] KVM: selftests: arm64: Make set_id_regs bitfield
 validatity checks non-fatal
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[01-05 16:45]** Re: [PATCH v3 4/4] KVM: selftests: arm64: Skip all 32 bit IDs when
 set_id_regs is aarch64 only
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[01-05 17:00]** Re: [PATCH v3 4/4] KVM: selftests: arm64: Skip all 32 bit IDs when
 set_id_regs is aarch64 only
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[01-10 02:22]** Re: [PATCH v3 0/4] KVM: arm64: pKVM fixes
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 12: [PATCH kvmtool v4 15/15] arm64: smccc: Start sending PSCI to userspace

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 08 Jan 2026 14:14:08 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于一个补丁（patch），其内容为“[PATCH kvmtool v4 15/15] arm64: smccc: 开始将 PSCI 发送到用户空间”。该补丁旨在通过 SMCCC 接口将 PSCI 调用转发到用户空间，改变了默认行为。

在之前的讨论中，Marc Zyngier 指出该补丁实际上是关于 PSCI，而非 SMCCC，并强调希望保持内核中 PSCI 的默认实现，以避免在旧内核上出现静默失败的问题。他建议对补丁进行修改，以便用户可以选择使用用户空间处理 PSCI。

本周的新讨论中，Suzuki K Poulose 表示同意 Marc 的建议，并承诺会进行相应的修改。Aneesh Kumar K.V 提出了关于 RHI（Realm Hypervisor Interface）处理的建议，认为 RHI 调用应始终由 VMM（虚拟机监控器）处理，而与 PSCI 的处理是不同的。Suzuki 也同意了这一观点，并讨论了如何重命名相关的过滤器结构，以便更好地管理 PSCI 和 RHI 的调用。

总体来看，本周的讨论集中在如何优化补丁的实现细节上，以及确保不同接口的处理逻辑清晰分开。

#### 📝 邮件列表

1. **[01-08 14:14]** Re: [PATCH kvmtool v4 15/15] arm64: smccc: Start sending PSCI to userspace
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-08 14:23]** Re: [PATCH kvmtool v4 15/15] arm64: smccc: Start sending PSCI to
 userspace
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
3. **[01-09 08:06]** Re: [PATCH kvmtool v4 15/15] arm64: smccc: Start sending PSCI to
 userspace
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
4. **[01-09 10:21]** Re: [PATCH kvmtool v4 15/15] arm64: smccc: Start sending PSCI to
 userspace
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
5. **[01-09 16:13]** Re: [PATCH kvmtool v4 15/15] arm64: smccc: Start sending PSCI to
 userspace
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
6. **[01-09 17:14]** Re: [PATCH kvmtool v4 15/15] arm64: smccc: Start sending PSCI to
 userspace
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 13: [PATCH v3 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in
 host handler

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 8 Jan 2026 15:26:21 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在支持 FFA_MSG_SEND_DIRECT_REQ 的主机处理程序。补丁的主要内容是增强 KVM 对直接请求消息的处理能力，以便更好地支持 ARM 的功能。

在之前的讨论中，参与者们关注了补丁的实现细节，包括如何处理标志位（flags）以及 HOST_FFA_ID 的使用。Will Deacon 提出了一些优化建议，例如检查标志位是否为零，并询问了传递 HOST_FFA_ID 的目的。此外，他还指出了一些代码中的冗余部分，建议简化逻辑。

在本周的新讨论中，Sebastian Ene 和 Will Deacon 继续探讨了补丁的细节。Sebastian 同意简化代码，并解释了在 Android 内核中验证发送者的重要性，以防止身份冒充。Will 进一步提出，未来如果添加新的消息类型，当前的实现可能会更具鲁棒性，并强调了验证发送者的必要性。

总体来看，本周的讨论集中在补丁的优化和安全性验证上，参与者们达成了一些共识，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[01-08 15:26]** Re: [PATCH v3 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in
 host handler
   - 发件人: Will Deacon <will@kernel.org>
2. **[01-08 15:30]** Re: [PATCH v3 2/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Will Deacon <will@kernel.org>
3. **[01-09 11:18]** Re: [PATCH v3 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in
 host handler
   - 发件人: Sebastian Ene <sebastianene@google.com>
4. **[01-09 11:37]** Re: [PATCH v3 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in
 host handler
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 14: [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock across
 IRTE updates in IOMMU

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 22 Dec 2025 09:16:55 +0000

#### 🤖 AI 总结

在本次邮件讨论中，主题为“[PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock across IRTE updates in IOMMU”的补丁旨在解决在使用AMD SVM和AVIC时，可能出现的锁依赖问题。历史讨论中，Ankit Soni提到在特定环境下（使用VFIO直通设备）观察到了锁依赖警告，可能导致死锁的风险，Paolo Bonzini对此表示关注，并详细分析了死锁的可能性。

在本周的新讨论中，Thomas Gleixner对Paolo的担忧表示反对，认为在隔离场景中，唤醒操作的延迟是合理的，并指出这种情况在内核的IRQ核心中并不是唯一的锁链问题。他强调，irq_set_affinity_locked()函数在持有desc::lock时调用，可能导致rq::lock的获取，这种情况在过去15年中一直存在，因此不应将其视为内核或IRQ的错误。

总体来看，本周的讨论主要集中在对死锁风险的不同看法上，Thomas Gleixner坚持认为现有机制是合理的，并对之前的警告表示质疑。

#### 📝 邮件列表

1. **[12-22 09:16]** Re: [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock across
 IRTE updates in IOMMU
   - 发件人: Ankit Soni <Ankit.Soni@amd.com>
2. **[12-22 15:09]** possible deadlock due to irq_set_thread_affinity() calling into the
 scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock
 across IRTE updates in IOMMU)
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
3. **[01-08 22:28]** Re: possible deadlock due to irq_set_thread_affinity() calling into
 the scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold
 ir_list_lock across IRTE updates in IOMMU)
   - 发件人: Thomas Gleixner <tglx@kernel.org>
4. **[01-08 22:53]** Re: possible deadlock due to irq_set_thread_affinity() calling into
 the scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold
 ir_list_lock across IRTE updates in IOMMU)
   - 发件人: Thomas Gleixner <tglx@kernel.org>

---

### Thread 15: [PATCH] KVM: arm64: gic: Check for vGICv3 when clearing TWI

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 6 Jan 2026 16:52:10 +0000

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: gic: Check for vGICv3 when clearing TWI”，主要讨论在清除 TWI 时显式检查 vGIC 是否为 v3 的问题。

在本周的新讨论中，Sascha Bischoff 提出了一个补丁，建议在禁用 TWI 时检查 vgic 是否为 v3。未进行此检查可能导致使用错误的 vgic CPU IF union，从而引发不期望的行为。补丁内容包括在 `kvm_vcpu_should_clear_twi` 函数中增加了一行代码，以确保在特定条件下才会清除 TWI。

Marc Zyngier 对该补丁表示认可，并提出了对类似问题的关注，表示希望能发现更多类似的情况。Oliver Upton 则确认该补丁已被应用到修复列表中，并感谢 Sascha 的贡献。

综上所述，本周讨论的重点在于补丁的提出及其重要性，参与者对补丁的积极反馈表明该修改将有助于提升 KVM 的稳定性与可靠性。

#### 📝 邮件列表

1. **[01-06 16:52]** [PATCH] KVM: arm64: gic: Check for vGICv3 when clearing TWI
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[01-06 18:13]** Re: [PATCH] KVM: arm64: gic: Check for vGICv3 when clearing TWI
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-10 02:22]** Re: [PATCH] KVM: arm64: gic: Check for vGICv3 when clearing TWI
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 16: [PATCH] KVM: arm64: nv: Respect stage-2 write permssion when setting stage-1 AF

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  8 Jan 2026 12:42:30 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要涉及在设置 stage-1 访问标志时，如何遵循 stage-2 的写权限。

**原始补丁内容**：
补丁的核心是确保在更新 stage-1 描述符的访问标志时，必须具备 stage-2 的写权限。当前 KVM 的软件页表转换（PTW）并未强制执行这一点，因此补丁通过生成 stage-2 权限故障来解决这一问题。

**之前讨论要点**：
在本周之前并没有相关的历史讨论，所有讨论均集中在本周的补丁及其影响上。

**本周的新讨论与进展**：
本周的讨论中，Oliver Upton 提交了补丁，并详细说明了实现细节。Marc Zyngier 对该补丁进行了审核并表示支持。最终，Oliver Upton 确认该补丁已被应用于修复分支，标志着这一问题的解决。补丁的提交和审核过程显示出社区对提升 KVM 稳定性和安全性的重视。

#### 📝 邮件列表

1. **[01-08 12:42]** [PATCH] KVM: arm64: nv: Respect stage-2 write permssion when setting stage-1 AF
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[01-09 11:31]** Re: [PATCH] KVM: arm64: nv: Respect stage-2 write permssion when setting stage-1 AF
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-10 02:22]** Re: [PATCH] KVM: arm64: nv: Respect stage-2 write permssion when setting stage-1 AF
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 17: [PATCH v4 0/2] KVM: arm64: Support FF-A direct messaging
 interfaces

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 09 Jan 2026 22:34:24 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A（Firmware Framework for Arm）直接消息接口的两个补丁（patch）。 

**原始补丁内容**：
补丁主要包括对 FFA_MSG_SEND_DIRECT_REQ 和 FFA_MSG_SEND_DIRECT_REQ2 接口的支持，目的是允许主机处理直接消息，并在 FF-A 1.2 版本中引入新的消息接口。

**历史讨论要点**：
在之前的讨论中，第二个补丁曾被删除，原因是缺乏明确的使用案例。现在，随着 TPM 设备在使用 pkvm 启动时的需求明确，重新引入了该补丁。

**本周新讨论与进展**：
本周的讨论中，Per Larsen 提出了两个补丁的更新，分别是：
1. **补丁 1/2**：支持 FFA_MSG_SEND_DIRECT_REQ，确保主机不发送框架消息，并进行相应的过滤。
2. **补丁 2/2**：支持 FFA_MSG_SEND_DIRECT_REQ2，更新了主机的处理逻辑，确保在 FF-A 1.2 版本中可以正确处理该请求。

这两个补丁经过测试，并在 QEMU 上成功启动 Android，得到了相关人员的审核和认可。整体来看，本周的讨论集中在补丁的实现细节和测试结果上，推进了对 FF-A 接口的支持。

#### 📝 邮件列表

1. **[01-09 22:34]** [PATCH v4 0/2] KVM: arm64: Support FF-A direct messaging
 interfaces
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[01-09 22:34]** [PATCH v4 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in host
 handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[01-09 22:34]** [PATCH v4 2/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>

---

### Thread 18: [PATCH v2 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF
 events

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 24 Dec 2025 14:15:16 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下启用 HDBSS（Hardware Debugging and Boot State Support）功能及处理 HDBSSF（HDBSS Fault）事件的补丁（PATCH v2 4/5）。

在历史讨论中，参与者 Robert Hoo 提出了在 `ram_save_cleanup` 函数中，当禁用 HDBSS 功能时，应该检查 `size` 是否为 0，以决定是否执行后续操作。Tian Zheng 进一步建议在分配内存之前，检查 `kvm->arch.enable_hdbss` 是否已设置，以避免不必要的内存分配。这些讨论强调了在设计 KVM API 时，不能仅依赖于 QEMU 的实现流程。

在本周的新讨论中，Tian Zheng 确认最新的 v3 补丁已经修复了之前提到的问题，通过检查条件 `size > 0 && kvm->arch.enable_hdbss`，在满足条件时，函数会立即返回，而不再执行内存分配。这表明补丁的改进有效地解决了之前的设计缺陷。

#### 📝 邮件列表

1. **[12-24 14:15]** Re: [PATCH v2 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF
 events
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
2. **[12-28 21:21]** Re: [PATCH v2 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF
 events
   - 发件人: Robert Hoo <robert.hoo.linux@gmail.com>
3. **[01-09 15:52]** Re: [PATCH v2 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF
 events
   - 发件人: Tian Zheng <zhengtian10@huawei.com>

---

### Thread 19: [PATCH 15/32] KVM: arm64: gic-v5: Implement direct injection of
 PPIs

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 7 Jan 2026 14:50:38 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下实现 GICv5（通用中断控制器版本5）中 PPIs（私有中断）的直接注入。原始的 patch 旨在改进 PPIs 的处理，以提高虚拟化性能和准确性。

在之前的讨论中，Marc Zyngier 提到了一些潜在的问题，特别是关于检查条件的有效性，认为在当前实现中某些检查可能不再适用，因此决定删除这些检查。Sascha Bischoff 也参与了讨论，确认了对架构定时器的处理逻辑，强调在非嵌套的虚拟机中，主机和客机的定时器 PPIs 应该保持一一对应关系。

本周的新讨论中，Sascha Bischoff 对 patch 进行了进一步的修改，优化了 PPIs 的优先级同步逻辑，确保只有在进入 WFI（等待中断）时才进行同步，并且只同步那些实际暴露给客机的 PPIs。此外，他还对代码结构进行了重构，以提高可读性，避免不必要的缩进和复杂性。整体来看，本周的进展集中在代码的优化和逻辑清晰度的提升上。

#### 📝 邮件列表

1. **[01-07 14:50]** Re: [PATCH 15/32] KVM: arm64: gic-v5: Implement direct injection of
 PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[01-07 15:59]** Re: [PATCH 18/32] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[01-07 16:28]** Re: [PATCH 17/32] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 20: [PATCH v2] KVM: arm64: Remove unused vcpu_{clear,set}_wfx_traps()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  9 Jan 2026 16:02:26 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 arm64 架构中未使用函数的补丁。补丁内容为删除两个未使用的函数 `vcpu_clear_wfx_traps()` 和 `vcpu_set_wfx_traps()`，这些函数自从提交 0b5afe05377d7 以来就没有被使用过。

在历史讨论中，补丁的提出者 Dongxu Sun 指出这两个函数的冗余性，并在补丁中提供了相应的代码删除。补丁经过了 Zenghui Yu 的审核，确认其合理性。

在本周的新讨论中，Dongxu Sun 提交了补丁的第二版，更新了主题和提交信息。Oliver Upton 在随后的邮件中确认已将该补丁应用到修复分支中，并感谢了 Dongxu Sun 的贡献。这表明该补丁得到了认可并成功合并，进一步清理了代码库中的冗余部分。

#### 📝 邮件列表

1. **[01-09 16:02]** [PATCH v2] KVM: arm64: Remove unused vcpu_{clear,set}_wfx_traps()
   - 发件人: Dongxu Sun <sundongxu1024@163.com>
2. **[01-10 02:22]** Re: [PATCH v2] KVM: arm64: Remove unused vcpu_{clear,set}_wfx_traps()
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 21: [PATCH] KVM: arm64: Don't blindly set set PSTATE.PAN on guest exit

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  7 Jan 2026 12:46:00 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下处理 PSTATE.PAN（Process State Register中的一个标志位）的问题。Marc Zyngier 提出的补丁（patch）旨在修复在从虚拟机（guest）退出时盲目设置 PSTATE.PAN 的问题。

在历史讨论中，Marc 指出在 nVHE（non-Virtual Hypervisor Extension）配置下，EL2（Exception Level 2）并不支持 PAN，因此在此情况下设置 PSTATE.PAN 是没有意义的。此外，如果没有正确处理 CONFIG_ARM64_PAN 的设置，可能会导致使用虚拟机的 PSTATE.PAN 值，从而在用户空间访问时引发错误。补丁通过在运行 VHE 时始终设置 PAN 的值来解决这一问题，而在 nVHE 下则忽略该设置。

本周的讨论中，Marc Zyngier 提交的补丁得到了 Oliver Upton 的确认，并已被应用到修复补丁中。补丁的主要内容包括对相关代码的修改，以确保在合适的条件下正确设置 PSTATE.PAN，从而避免潜在的系统崩溃。此补丁的成功应用标志着这一问题的解决。

#### 📝 邮件列表

1. **[01-07 12:46]** [PATCH] KVM: arm64: Don't blindly set set PSTATE.PAN on guest exit
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-10 02:22]** Re: [PATCH] KVM: arm64: Don't blindly set set PSTATE.PAN on guest exit
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 22: [PATCH] KVM: arm64: remove unused vcpu_{clear,set}_wfx_traps()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  9 Jan 2026 10:58:37 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于移除 KVM（Kernel-based Virtual Machine）在 arm64 架构中未使用的函数 `vcpu_{clear,set}_wfx_traps()` 的补丁。该补丁由 Dongxu Sun 提出，目的是清理代码，因为这两个函数自从提交 0b5afe05377d7 以来就没有被使用过。

在之前的讨论中，虽然没有具体的历史邮件记录，但可以推测出该补丁的提出是基于对代码整洁性和维护性的考虑。移除未使用的代码可以减少潜在的混淆和维护成本。

在本周的新讨论中，Dongxu Sun 提交了补丁，并详细说明了移除这两个函数的原因。Zenghui Yu 对该补丁进行了审查，提出了一个小的修改建议，建议在主题中将“remove”改为“Remove”，并指出了代码检查工具的警告，建议保持每行不超过 75 个字符。最终，Zenghui Yu 表示支持该补丁，并给予了“Reviewed-by”的标记，表明他认为该补丁是合适的。

综上所述，本周的讨论主要集中在补丁的审查和小的格式修改建议上，补丁本身旨在提升代码的整洁性。

#### 📝 邮件列表

1. **[01-09 10:58]** [PATCH] KVM: arm64: remove unused vcpu_{clear,set}_wfx_traps()
   - 发件人: Dongxu Sun <sundongxu1024@163.com>
2. **[01-09 14:06]** Re: [PATCH] KVM: arm64: remove unused vcpu_{clear,set}_wfx_traps()
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

### Thread 23: [PATCH v6 39/44] KVM: VMX: Bug the VM if either MSR auto-load
 list is full

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 8 Jan 2026 12:04:11 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）中的一个补丁，具体是「[PATCH v6 39/44] KVM: VMX: Bug the VM if either MSR auto-load list is full」。该补丁的目的是在 MSR（模型特定寄存器）自动加载列表满时，向虚拟机报告错误。

在历史讨论中，没有提供具体的背景信息或之前的讨论内容，因此我们只能从本周的新讨论中获取信息。

本周的讨论主要集中在补丁的意图和实现细节上。参与者 Sean Christopherson 和 Dapeng Mi 进行了简短的交流，Dapeng Mi 提到补丁的设计是为了确保与上方的“guest”行对齐。Sean Christopherson 对此表示感谢，确认了这一点。

总体来看，本周的讨论没有提出新的问题或争议，而是明确了补丁的设计意图，显示出参与者之间的良好沟通。

#### 📝 邮件列表

1. **[01-08 12:04]** Re: [PATCH v6 39/44] KVM: VMX: Bug the VM if either MSR auto-load
 list is full
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[01-09 08:29]** Re: [PATCH v6 39/44] KVM: VMX: Bug the VM if either MSR auto-load
 list is full
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>

---

### Thread 24: [PATCH v8 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 23 Dec 2025 17:33:36 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于支持 Armv8.7 架构中的 FEAT_{LS64, LS64_V} 特性的补丁（PATCH v8 0/7）。该补丁的主要内容包括：在 CPU 特性列表中添加识别和启用 FEAT_{LS64, LS64_V}，通过 HWCAP3 和 cpuinfo 向用户空间暴露 FEAT_LS64 的支持，增加相关的硬件能力测试，以及在虚拟机中处理不支持的内存访问（正常/不可缓存）。

在历史讨论中，Zhou Wang 提出了该补丁的背景，强调了这一特性在用户空间驱动中的实际应用场景。补丁旨在提升对新指令的支持，以便更好地利用 Armv8.7 的新功能。

在本周的新讨论中，Zhou Wang 对该补丁进行了跟进，询问是否还有其他评论，并希望能在本周期内合并该补丁。整体来看，讨论显示出对该补丁的关注和期待，表明参与者希望尽快推进此项工作。

#### 📝 邮件列表

1. **[12-23 17:33]** [PATCH v8 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[01-08 17:20]** Re: [PATCH v8 0/7] Add support for FEAT_{LS64, LS64_V} and related
 tests
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 25: (subset) [PATCH v2 1/6] KVM: arm64: Fix EL2 S1 XN handling for hVHE setups

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 10 Jan 2026 02:22:44 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM 在 arm64 架构下的 EL2 S1 XN 处理，特别是针对 hVHE（高虚拟化扩展）设置的相关问题。邮件中提到的补丁（patch）是“[PATCH v2 1/6] KVM: arm64: Fix EL2 S1 XN handling for hVHE setups”，旨在解决在特定虚拟化环境中可能出现的处理错误。

在历史讨论中，没有提供具体的背景信息或之前的讨论内容，因此我们无法了解补丁的详细历史背景。

在本周的新讨论中，参与者 Oliver Upton 提到该补丁已被应用到修复列表中，表示该问题得到了认可并已采取措施进行修复。这表明开发团队对该补丁的有效性和必要性达成了一致，并已开始实施相应的修复。整体来看，本周的讨论主要集中在补丁的应用和确认上。

#### 📝 邮件列表

1. **[01-10 02:22]** Re: (subset) [PATCH v2 1/6] KVM: arm64: Fix EL2 S1 XN handling for hVHE setups
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 26: [PATCH] KVM: arm64: Fix error checking for FFA_VERSION

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 8 Jan 2026 15:47:41 +0000

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: Fix error checking for FFA_VERSION”，主要讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 FFA_VERSION 的错误检查。

在本周的新讨论中，参与者 Will Deacon 对该补丁表示认可，并给予了“已确认”（Acked-by）的反馈。这表明补丁得到了支持，可能会在后续版本中合并。

由于该邮件列表没有提供历史讨论的内容，因此我们无法了解补丁的详细背景或之前的讨论要点。总体来看，本周的进展是补丁得到了认可，显示出对修复工作的积极态度。

#### 📝 邮件列表

1. **[01-08 15:47]** Re: [PATCH] KVM: arm64: Fix error checking for FFA_VERSION
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 27: [PATCH] KVM: arm64: Fix error checking for FFA_VERSION

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 8 Jan 2026 15:47:13 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复对 FFA_VERSION 的错误检查。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了处理在调用 FFA_VERSION 时可能出现的错误情况。Marc Zyngier 提到，针对嵌套的 !FFA 路径可能会导致 kvm_smccc_call_handler() 返回 KVM_SMCCC_FILTER_DENY，从而返回 SMCCC_RET_NOT_SUPPORTED，这可能会隐藏代理代码中的错误。

在本周的新讨论中，Will Deacon 对此进行了进一步分析，确认了这种行为的不同可能是由于错误检查不充分导致的。他指出，补丁的修复措施在这种情况下依然有效，因为它会忽略高32位，从而避免潜在的错误。

总结而言，此次讨论围绕 KVM 的 FFA_VERSION 错误检查补丁展开，参与者分析了可能的错误来源及补丁的有效性，推动了对该问题的深入理解和解决方案的确认。

#### 📝 邮件列表

1. **[01-08 15:47]** Re: [PATCH] KVM: arm64: Fix error checking for FFA_VERSION
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 28: [PATCH v2 03/11] coco: guest: arm64: Add support for guest
 initiated TDI bind/unbind

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 8 Jan 2026 15:32:14 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于一个补丁（patch），其内容为“coco: guest: arm64: 添加对来宾发起的 TDI 绑定/解绑的支持”。该补丁旨在增强 ARM64 架构下的虚拟化支持，具体涉及到来宾操作系统如何处理 TDI（Transport Driver Interface）绑定和解绑的功能。

在历史讨论中，并没有提供具体的背景信息或之前的讨论要点，邮件线程中仅包含本周的新讨论。

本周的讨论中，参与者 Will Deacon 对补丁提出了质疑，建议将其作为 RFC（请求反馈）进行发布，理由是该补丁的合并似乎不太合适。这表明当前对该补丁的接受度存在不确定性，可能需要更多的反馈和讨论，以确保其在合并前的可行性和必要性。

总结而言，本周的讨论集中在对补丁的合并是否合适的质疑上，建议将其转为 RFC 以获取更多意见。

#### 📝 邮件列表

1. **[01-08 15:32]** Re: [PATCH v2 03/11] coco: guest: arm64: Add support for guest
 initiated TDI bind/unbind
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 29: [PATCH kvmtool 00/15] arm64: Handle PSCI calls in userspace

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 08 Jan 2026 14:19:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM 工具的补丁系列，主要目的是在用户空间处理 ARM64 架构下的 PSCI 调用。该补丁系列包含 15 个补丁，旨在改善 ARM64 系统的虚拟化性能和功能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出补丁的初衷是为了优化 PSCI（电源管理接口）在用户空间的处理方式，以提升系统的整体效率和响应能力。

在本周的新讨论中，Marc Zyngier 对补丁的整体质量表示认可，并指出在补丁的首尾部分有一些需要注意的地方。他表示补丁在经过这些小的调整后，整体看起来相当不错，并给予了“Reviewed-by”的标记，表明他支持这一补丁的合并。

总结来说，本周的讨论主要集中在对补丁的审查和反馈上，Marc Zyngier 的认可为后续的合并提供了积极的信号。

#### 📝 邮件列表

1. **[01-08 14:19]** Re: [PATCH kvmtool 00/15] arm64: Handle PSCI calls in userspace
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 30: [PATCH kvmtool v4 01/15] Allow pausing the VM from vcpu thread

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 08 Jan 2026 14:19:12 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（patch），其内容为“允许从虚拟CPU线程暂停虚拟机”。该补丁旨在增强KVM工具的功能，使得用户能够在虚拟CPU线程中暂停虚拟机的运行。

在之前的讨论中，虽然没有具体的历史邮件记录，但可以推测该补丁的提出是为了改善虚拟机的管理和控制能力，尤其是在处理多线程环境下的虚拟机时。

在本周的新讨论中，Marc Zyngier对补丁中的一个实现细节提出了疑问。他询问为什么在函数结束时需要对某个状态进行两次设置，这表明他对补丁的实现逻辑存在疑虑。这一问题可能影响到补丁的最终效果和稳定性，提示开发者需要进一步审视代码的设计。

总体来看，本周的讨论集中在补丁的实现细节上，反映出对代码质量和逻辑一致性的关注。

#### 📝 邮件列表

1. **[01-08 14:19]** Re: [PATCH kvmtool v4 01/15] Allow pausing the VM from vcpu thread
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 31: [PATCH RESEND v2 02/12] firmware: smccc: coco: Manage arm-smccc
 platform device and CCA auxiliary drivers

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 06 Jan 2026 18:03:27 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（patch），其内容为“[PATCH RESEND v2 02/12] firmware: smccc: coco: 管理 arm-smccc 平台设备和 CCA 辅助驱动”。该补丁旨在改进对 ARM SMCCC（Secure Monitor Call Convention）平台设备的管理，特别是与 CCA（Common Control Architecture）相关的辅助驱动。

在历史讨论中，并没有提供具体的背景信息或之前的讨论要点，因此我们无法了解该补丁的详细背景或先前的讨论内容。

在本周的新讨论中，参与者 Aneesh Kumar K.V 向邮件列表发送了一封提醒邮件，询问对该补丁的反馈。他表示希望能收到更多的意见和建议，以便进一步完善补丁。这表明该补丁仍在等待社区的反馈和讨论，尚未进入最终审核或合并阶段。

总的来说，目前的进展是补丁仍在等待反馈，参与者积极寻求社区的意见。

#### 📝 邮件列表

1. **[01-06 18:03]** Re: [PATCH RESEND v2 02/12] firmware: smccc: coco: Manage arm-smccc
 platform device and CCA auxiliary drivers
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>

---

## 📌 RFC

共 6 个 thread

---

### Thread 1: [RFC PATCH v6 29/35] KVM: arm64: Pin the SPE buffer in the host
 and map it at stage 2

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 9 Jan 2026 16:29:33 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在将 SPE（Statistical Profiling Extension）缓冲区固定在主机上并在第二阶段进行映射。

在历史讨论中，补丁的主要目的是优化 SPE 缓冲区的管理，以提高性能。然而，参与者 Alexandru Elisei 提出的问题是，当前驱动在每次进程切换时都会启用和禁用缓冲区，导致性能显著下降，尤其是在使用较大缓冲区时。具体来说，使用 `perf` 命令时，执行时间大幅增加，且频繁的上下文切换导致了严重的性能瓶颈。

在本周的新讨论中，Alexandru Elisei 强调了在没有有效的启发式方法来保持缓冲区固定的情况下，当前实现几乎无法使用。James Clark 补充指出，通常情况下，增加缓冲区大小是应对高性能开销的常见做法，但在虚拟机中，这种做法反而会加剧问题，导致性能进一步下降。

总的来看，当前补丁在实际应用中面临显著的性能挑战，参与者们呼吁寻找更有效的解决方案，以改善缓冲区的管理和性能表现。

#### 📝 邮件列表

1. **[01-09 16:29]** Re: [RFC PATCH v6 29/35] KVM: arm64: Pin the SPE buffer in the host
 and map it at stage 2
   - 发件人: James Clark <james.clark@linaro.org>
2. **[01-09 16:35]** Re: [RFC PATCH v6 29/35] KVM: arm64: Pin the SPE buffer in the host
 and map it at stage 2
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 2: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 9 Jan 2026 16:29:50 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中为 arm64 架构添加 CONFIG_KVM_ARM_SPE Kconfig 选项的 RFC patch（请求反馈的补丁）。该补丁旨在提供对 ARM 处理器的性能监控扩展（SPE）的支持。

在历史讨论中，尚未有相关的背景信息或补丁内容被提及，因此我们无法提供具体的历史讨论要点。

本周的讨论中，参与者 James Clark 对补丁提出了意见，指出当前默认配置为内置（built-in）可能不利于用户的采用，建议将其改为模块（module）配置。他提到，许多用户在尝试使其工作时会遇到困难，如果无法避免内置配置，建议至少提供调试信息，以说明启用失败的原因。这一反馈反映了对用户友好性和易用性的关注，可能会影响后续补丁的修改方向。

#### 📝 邮件列表

1. **[01-09 16:29]** Re: [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig
 option
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 3: [RFC PATCH v6 14/35] KVM: arm64: Add SPE VCPU device attribute to
 set the max buffer size

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 9 Jan 2026 16:29:43 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中为 arm64 架构添加 SPE（Sampling Processor Event）虚拟 CPU 设备属性，以设置最大缓冲区大小的补丁（RFC PATCH v6 14/35）。

在历史讨论中，补丁的主要目的是为 KVM 的 SPE 功能提供一个机制，以便用户能够指定最大缓冲区大小，从而优化性能和资源使用。然而，之前的讨论并未详细记录，因此我们无法提供更多背景信息。

在本周的新讨论中，参与者 James Clark 提到他在使用该补丁时遇到了一些问题，尤其是在不同的缓冲区大小下运行时，某些情况下会出现错误信息。Clark 还提出了一些建议，例如在文档中使用“Initialised with SPE”来替代“ASSIGN_SPU”，以提高可理解性。此外，他对缓冲区使用的描述提出了疑问，认为需要更清晰地阐明最大缓冲区大小的限制来源。

总体来看，本周的讨论集中在补丁的实际应用和文档表述的清晰度上，参与者对补丁的稳定性和使用方式进行了探讨，并提出了改进建议。

#### 📝 邮件列表

1. **[01-09 16:29]** Re: [RFC PATCH v6 14/35] KVM: arm64: Add SPE VCPU device attribute to
 set the max buffer size
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 4: [RFC PATCH v6 19/35] KVM: arm64: Trap PMBIDR_EL1 and PMSIDR_EL1

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 9 Jan 2026 16:29:37 +0000

#### 🤖 AI 总结

在本邮件线程中，讨论的主题是关于一个名为「[RFC PATCH v6 19/35] KVM: arm64: Trap PMBIDR_EL1 and PMSIDR_EL1」的补丁。该补丁旨在处理 ARM64 架构中的 PMBIDR_EL1 和 PMSIDR_EL1 寄存器，以便在 KVM 虚拟化环境中更好地管理这些寄存器的值。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了提升 KVM 对 ARM64 架构的支持，尤其是在寄存器管理方面。参与者可能之前讨论了如何在虚拟机中正确报告和使用这些寄存器的值。

在本周的新讨论中，参与者 James Clark 对补丁提出了疑问，指出如果硬件中的 PMBIDR 值已经符合虚拟机的需求，那么这个补丁的必要性可能并不强。他建议可以将这个功能作为后续的增强来实现，以便在更多场景中使用。这表明当前补丁的实施可能存在一定的灵活性，且在实际应用中可能需要进一步的评估和讨论。

#### 📝 邮件列表

1. **[01-09 16:29]** Re: [RFC PATCH v6 19/35] KVM: arm64: Trap PMBIDR_EL1 and PMSIDR_EL1
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 5: [RFC PATCH v6 17/35] KVM: arm64: Add writable SPE system
 registers to VCPU context

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 5 Jan 2026 16:42:34 +0000

#### 🤖 AI 总结

本邮件主题为“[RFC PATCH v6 17/35] KVM: arm64: Add writable SPE system registers to VCPU context”，主要讨论在 KVM 的 arm64 架构中，为 VCPU 上下文添加可写的 SPE 系统寄存器的补丁。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁旨在增强 KVM 对 SPE（可扩展性能监控）的支持，以便更好地管理和利用系统寄存器。

本周的新讨论中，参与者 Alexandru Elisei 对于之前的讨论做出了回应，表示将会修复相关问题，显示出对补丁的积极反馈和进一步改进的意愿。虽然没有详细的技术细节，但这一回应表明了对补丁的认可，并承诺将进行必要的修改。

总体来看，本周的讨论集中在补丁的修正和完善上，参与者之间的互动表明了对该功能增强的重视。

#### 📝 邮件列表

1. **[01-05 16:42]** Re: [RFC PATCH v6 17/35] KVM: arm64: Add writable SPE system
 registers to VCPU context
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 6: [RFC PATCH v6 16/35] KVM: arm64: Advertise SPE version in
 ID_AA64DFR0_EL1.PMSver

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 5 Jan 2026 16:42:09 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构中如何在 ID_AA64DFR0_EL1.PMSver 中宣传 SPE（可编程事件计数器）版本的 RFC PATCH（请求反馈补丁）第 16/35 部分。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出该补丁旨在通过限制用户空间可以设置的 SPE 版本，确保虚拟机（VM）使用的 SPU（特殊处理单元）版本的安全性。补丁的初衷是通过与 PMUVer 的处理方式相似来实现这一点。

在本周的新讨论中，参与者 Alexandru Elisei 和 Suzuki K Poulose 进行了交流。Alexandru 承认在补丁中存在一些误解，特别是在 cpufeature.c 中的 FTR_LOWER_SAFE 处理上。他意识到某些 SPE 版本可能会引入新的字段，而 KVM 无法在用户空间设置较低版本的情况下隐藏这些字段。因此，他决定暂时不允许用户空间写入 PMSVer，并表示会在未来重新考虑这一点。整体来看，本周的讨论集中在对补丁的细节修正和对用户空间权限的重新评估上。

#### 📝 邮件列表

1. **[01-05 16:42]** Re: [RFC PATCH v6 16/35] KVM: arm64: Advertise SPE version in
 ID_AA64DFR0_EL1.PMSver
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: [kvmtool PATCH v5 00/15] arm64: Handle PSCI calls in userspace

**📧 邮件数**: 16 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  8 Jan 2026 17:57:38 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM 工具的 PSCI 调用处理的补丁系列（PATCH v5）。该系列补丁的目标是实现用户空间对 PSCI 调用的支持，主要通过 SMCCC 过滤功能来处理这些调用。

**原始补丁/问题内容**：
补丁系列的核心是实现用户空间对 PSCI 调用的处理，包括 CPU 的挂起、开启、亲和性信息和系统关机等功能。

**之前讨论要点**：
在之前的版本中，开发者们讨论了如何在用户空间中处理 PSCI 调用的挑战，包括如何确保在多核环境中正确管理 vCPU 的状态，以及如何实现 SMCCC 过滤以将 PSCI 调用转发到用户空间。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上，包括：
1. 实现了 PSCI 的基本调用，如 CPU_SUSPEND、CPU_ON、AFFINITY_INFO 和 SYSTEM_{OFF,RESET}。
2. 通过 ioctl 调用 KVM_ARM_VCPU_INIT 来重置 vCPU，并在处理 CPU_ON 时确保目标 vCPU 的状态为停止。
3. 增加了对 PSCI 功能的查询支持，并实现了对亲和性信息的处理，确保在暂停 VM 的情况下安全执行。
4. 最后，补丁还设置了 SMCCC 过滤，以便将 PSCI 调用转发到用户空间。

整体来看，这些补丁为 KVM 工具的 ARM64 支持提供了重要的功能扩展，增强了其在虚拟化环境中的灵活性和可用性。

#### 📝 邮件列表

1. **[01-08 17:57]** [kvmtool PATCH v5 00/15] arm64: Handle PSCI calls in userspace
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
2. **[01-08 17:57]** [kvmtool PATCH v5 01/15] Allow pausing the VM from vcpu thread
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
3. **[01-08 17:57]** [kvmtool PATCH v5 02/15] update_headers: arm64: Track psci.h for PSCI definitions
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
4. **[01-08 17:57]** [kvmtool PATCH v5 03/15] update headers: Linux v6.18
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
5. **[01-08 17:57]** [kvmtool PATCH v5 04/15] Import arm-smccc.h from Linux v6.18
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
6. **[01-08 17:57]** [kvmtool PATCH v5 05/15] arm64: Stash kvm_vcpu_init for later use
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
7. **[01-08 17:57]** [kvmtool PATCH v5 06/15] arm64: Use KVM_SET_MP_STATE ioctl to power off non-boot vCPUs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[01-08 17:57]** [kvmtool PATCH v5 07/15] arm64: Expose ARM64_CORE_REG() for general use
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
9. **[01-08 17:57]** [kvmtool PATCH v5 08/15] arm64: Add support for finding vCPU for given MPIDR
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
10. **[01-08 17:57]** [kvmtool PATCH v5 09/15] arm64: Add skeleton implementation for PSCI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
11. **[01-08 17:57]** [kvmtool PATCH v5 10/15] arm64: psci: Implement CPU_SUSPEND
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
12. **[01-08 17:57]** [kvmtool PATCH v5 11/15] arm64: psci: Implement CPU_ON
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
13. **[01-08 17:57]** [kvmtool PATCH v5 12/15] arm64: psci: Implement AFFINITY_INFO
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
14. **[01-08 17:57]** [kvmtool PATCH v5 13/15] arm64: psci: Implement MIGRATE_INFO_TYPE
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
15. **[01-08 17:57]** [kvmtool PATCH v5 14/15] arm64: psci: Implement SYSTEM_{OFF,RESET}
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
16. **[01-08 17:57]** [kvmtool PATCH v5 15/15] arm64: smccc: Start sending PSCI to userspace
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

