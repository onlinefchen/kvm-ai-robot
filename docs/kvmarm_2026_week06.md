# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2026-02-09 00:31:17

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 142
- **总 Thread 数**: 17
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 16 threads (141 邮件)
- **GIT PULL**: 1 threads (1 邮件)

---

## 📌 PATCH

共 16 个 thread

---

### Thread 1: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code

**📧 邮件数**: 54 | **👥 参与者**: 3 | **📅 开始时间**: Tue,  3 Feb 2026 21:43:01 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 ARM MPAM（内存分区和监控）与 resctrl（资源控制）集成的多个补丁，主要集中在如何增强 ARM64 架构对 MPAM 的支持。

1. **原始补丁/问题内容**：补丁系列的目标是将 MPAM 功能与 resctrl 结合，使得用户空间能够通过 resctrl 接口访问 MPAM 的资源分配和监控功能。

2. **之前讨论要点**：之前的讨论中提到，MPAM 需要与 resctrl 的现有机制兼容，确保在不同硬件平台上能够正确地实现资源监控和分配。补丁中包含了对 MPAM 驱动的多项改进，包括对 MPAM 控制寄存器的访问、任务和 CPU 的 MPAM PARTID/PMG 值的设置等。

3. **本周的新讨论、进展或结论**：本周的讨论主要集中在补丁的细节上，包括对 MPAM 规范的支持、特定硬件的错误修复（如 NVIDIA T241 的多个补丁）、以及如何在不同的硬件上实现资源监控和分配。参与者对补丁进行了测试和审查，确保其在不同平台上的有效性和稳定性。此外，补丁还增加了对 MPAM 文档的初步支持，以帮助用户理解 MPAM 的功能和使用方法。

总体而言，该系列补丁的实施将使 ARM64 架构在资源管理和监控方面更具灵活性和可靠性。

#### 📝 邮件列表

1. **[02-03 21:43]** [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[02-03 21:43]** [PATCH v4 01/41] arm64/sysreg: Add MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[02-03 21:43]** [PATCH v4 02/41] KVM: arm64: Preserve host MPAM configuration when changing traps
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[02-03 21:43]** [PATCH v4 03/41] KVM: arm64: Make MPAMSM_EL1 accesses UNDEF
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[02-03 21:43]** [PATCH v4 04/41] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[02-03 21:43]** [PATCH v4 05/41] arm64: mpam: Re-initialise MPAM regs when CPU comes online
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[02-03 21:43]** [PATCH v4 06/41] arm64: mpam: Drop the CONFIG_EXPERT restriction
   - 发件人: Ben Horgan <ben.horgan@arm.com>
8. **[02-03 21:43]** [PATCH v4 07/41] arm64: mpam: Advertise the CPUs MPAM limits to the driver
   - 发件人: Ben Horgan <ben.horgan@arm.com>
9. **[02-03 21:43]** [PATCH v4 08/41] arm64: mpam: Add cpu_pm notifier to restore MPAM sysregs
   - 发件人: Ben Horgan <ben.horgan@arm.com>
10. **[02-03 21:43]** [PATCH v4 09/41] arm64: mpam: Initialise and context switch the MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
11. **[02-03 21:43]** [PATCH v4 10/41] arm64: mpam: Add helpers to change a task or cpu's MPAM PARTID/PMG values
   - 发件人: Ben Horgan <ben.horgan@arm.com>
12. **[02-03 21:43]** [PATCH v4 11/41] KVM: arm64: Force guest EL1 to use user-space's partid configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
13. **[02-03 21:43]** [PATCH v4 12/41] KVM: arm64: Use kernel-space partid configuration for hypercalls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
14. **[02-03 21:43]** [PATCH v4 13/41] arm_mpam: resctrl: Add boilerplate cpuhp and domain allocation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[02-03 21:43]** [PATCH v4 14/41] arm_mpam: resctrl: Sort the order of the domain lists
   - 发件人: Ben Horgan <ben.horgan@arm.com>
16. **[02-03 21:43]** [PATCH v4 15/41] arm_mpam: resctrl: Pick the caches we will use as resctrl resources
   - 发件人: Ben Horgan <ben.horgan@arm.com>
17. **[02-03 21:43]** [PATCH v4 16/41] arm_mpam: resctrl: Implement resctrl_arch_reset_all_ctrls()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
18. **[02-03 21:43]** [PATCH v4 17/41] arm_mpam: resctrl: Add resctrl_arch_get_config()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
19. **[02-03 21:43]** [PATCH v4 18/41] arm_mpam: resctrl: Implement helpers to update configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
20. **[02-03 21:43]** [PATCH v4 19/41] arm_mpam: resctrl: Add plumbing against arm64 task and cpu hooks
   - 发件人: Ben Horgan <ben.horgan@arm.com>
21. **[02-03 21:43]** [PATCH v4 20/41] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
22. **[02-03 21:43]** [PATCH v4 21/41] arm_mpam: resctrl: Convert to/from MPAMs fixed-point formats
   - 发件人: Ben Horgan <ben.horgan@arm.com>
23. **[02-03 21:43]** [PATCH v4 22/41] arm_mpam: resctrl: Add kunit test for control format conversions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
24. **[02-03 21:43]** [PATCH v4 23/41] arm_mpam: resctrl: Add rmid index helpers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
25. **[02-03 21:43]** [PATCH v4 24/41] arm_mpam: resctrl: Add kunit test for rmid idx conversions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
26. **[02-03 21:43]** [PATCH v4 25/41] arm_mpam: resctrl: Wait for cacheinfo to be ready
   - 发件人: Ben Horgan <ben.horgan@arm.com>
27. **[02-03 21:43]** [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
28. **[02-03 21:43]** [PATCH v4 27/41] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
29. **[02-03 21:43]** [PATCH v4 28/41] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
30. **[02-03 21:43]** [PATCH v4 29/41] arm_mpam: resctrl: Pre-allocate free running monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
31. **[02-03 21:43]** [PATCH v4 30/41] arm_mpam: resctrl: Allow resctrl to allocate monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
32. **[02-03 21:43]** [PATCH v4 31/41] arm_mpam: resctrl: Add resctrl_arch_rmid_read() and resctrl_arch_reset_rmid()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
33. **[02-03 21:43]** [PATCH v4 32/41] arm_mpam: resctrl: Update the rmid reallocation limit
   - 发件人: Ben Horgan <ben.horgan@arm.com>
34. **[02-03 21:43]** [PATCH v4 33/41] arm_mpam: resctrl: Add empty definitions for assorted resctrl functions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
35. **[02-03 21:43]** [PATCH v4 34/41] arm64: mpam: Select ARCH_HAS_CPU_RESCTRL
   - 发件人: Ben Horgan <ben.horgan@arm.com>
36. **[02-03 21:43]** [PATCH v4 35/41] arm_mpam: resctrl: Call resctrl_init() on platforms that can support resctrl
   - 发件人: Ben Horgan <ben.horgan@arm.com>
37. **[02-03 21:43]** [PATCH v4 36/41] arm_mpam: Add quirk framework
   - 发件人: Ben Horgan <ben.horgan@arm.com>
38. **[02-03 21:43]** [PATCH v4 37/41] arm_mpam: Add workaround for T241-MPAM-1
   - 发件人: Ben Horgan <ben.horgan@arm.com>
39. **[02-03 21:43]** [PATCH v4 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
40. **[02-03 21:43]** [PATCH v4 39/41] arm_mpam: Add workaround for T241-MPAM-6
   - 发件人: Ben Horgan <ben.horgan@arm.com>
41. **[02-03 21:43]** [PATCH v4 40/41] arm_mpam: Quirk CMN-650's CSU NRDY behaviour
   - 发件人: Ben Horgan <ben.horgan@arm.com>
42. **[02-03 21:43]** [PATCH v4 41/41] arm64: mpam: Add initial MPAM documentation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
43. **[02-05 14:08]** Re: [PATCH v4 06/41] arm64: mpam: Drop the CONFIG_EXPERT
 restriction
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
44. **[02-05 16:16]** Re: [PATCH v4 04/41] arm64: mpam: Context switch the MPAM registers
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
45. **[02-05 16:20]** Re: [PATCH v4 05/41] arm64: mpam: Re-initialise MPAM regs when CPU
 comes online
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
46. **[02-05 16:21]** Re: [PATCH v4 06/41] arm64: mpam: Drop the CONFIG_EXPERT restriction
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
47. **[02-05 16:50]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB'
 resource
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
48. **[02-05 16:54]** Re: [PATCH v4 08/41] arm64: mpam: Add cpu_pm notifier to restore
 MPAM sysregs
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
49. **[02-05 16:55]** Re: [PATCH v4 27/41] arm_mpam: resctrl: Add support for csu
 counters
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
50. **[02-05 16:55]** Re: [PATCH v4 09/41] arm64: mpam: Initialise and context switch the
 MPAMSM_EL1 register
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
51. **[02-05 16:56]** Re: [PATCH v4 10/41] arm64: mpam: Add helpers to change a task or
 cpu's MPAM PARTID/PMG values
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
52. **[02-05 16:57]** Re: [PATCH v4 41/41] arm64: mpam: Add initial MPAM documentation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
53. **[02-05 16:58]** Re: [PATCH v4 28/41] arm_mpam: resctrl: Pick classes for use as mbm
 counters
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
54. **[02-05 17:05]** Re: [PATCH v4 41/41] arm64: mpam: Add initial MPAM documentation
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>

---

### Thread 2: [PATCH v2 00/20] KVM: arm64: Generalise RESx handling

**📧 邮件数**: 24 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  2 Feb 2026 18:43:09 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构中处理 RESx（保留位）的一系列补丁。Marc Zyngier 提出了一个包含 20 个补丁的系列，旨在统一和简化 RESx 位的处理。

**原始问题**：
Marc 指出当前的 RESx 处理存在不一致，特别是在处理 RES1 位时，缺乏清晰的定义和统一的数据结构。补丁的目标是明确 RES1 位的定义，简化 RES0 和 RES1 位的管理，并消除复杂的 FIXED_VALUE 处理。

**历史讨论要点**：
在之前的讨论中，Marc 提到了一些具体的改进措施，包括简化 RES0 处理、清理相关的帮助函数、引入新的调试文件以便于检查 RESx 设置等。这些改进旨在降低配置约束的复杂性。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现上，包括：
1. 引入新的数据结构以同时跟踪 RES0 和 RES1 位。
2. 允许根据配置推断 RES1 位。
3. 处理 HCR_EL2 和 SCTLR_EL1 的 RES1 位。
4. 完全移除 FIXED_VALUE 的处理。
5. 添加了一个调试文件，以便于用户查看计算出的 RESx 值。

最终，Marc 表示这些补丁已被应用到下一步的开发中，得到了参与者的认可和测试反馈。整体上，这一系列补丁旨在提升 KVM 在 ARM64 上的稳定性和可维护性。

#### 📝 邮件列表

1. **[02-02 18:43]** [PATCH v2 00/20] KVM: arm64: Generalise RESx handling
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-02 18:43]** [PATCH v2 01/20] arm64: Convert SCTLR_EL2 to sysreg infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-02 18:43]** [PATCH v2 02/20] KVM: arm64: Remove duplicate configuration for SCTLR_EL1.{EE,E0E}
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-02 18:43]** [PATCH v2 03/20] KVM: arm64: Introduce standalone FGU computing primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-02 18:43]** [PATCH v2 04/20] KVM: arm64: Introduce data structure tracking both RES0 and RES1 bits
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-02 18:43]** [PATCH v2 05/20] KVM: arm64: Extend unified RESx handling to runtime sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-02 18:43]** [PATCH v2 06/20] KVM: arm64: Inherit RESx bits from FGT register descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-02 18:43]** [PATCH v2 07/20] KVM: arm64: Allow RES1 bits to be inferred from configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-02 18:43]** [PATCH v2 08/20] KVM: arm64: Correctly handle SCTLR_EL1 RES1 bits for unsupported features
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-02 18:43]** [PATCH v2 09/20] KVM: arm64: Convert HCR_EL2.RW to AS_RES1
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-02 18:43]** [PATCH v2 10/20] KVM: arm64: Simplify FIXED_VALUE handling
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[02-02 18:43]** [PATCH v2 11/20] KVM: arm64: Add REQUIRES_E2H1 constraint as configuration flags
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[02-02 18:43]** [PATCH v2 12/20] KVM: arm64: Add RES1_WHEN_E2Hx constraints as configuration flags
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[02-02 18:43]** [PATCH v2 13/20] KVM: arm64: Move RESx into individual register descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[02-02 18:43]** [PATCH v2 14/20] KVM: arm64: Simplify handling of HCR_EL2.E2H RESx
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[02-02 18:43]** [PATCH v2 15/20] KVM: arm64: Get rid of FIXED_VALUE altogether
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[02-02 18:43]** [PATCH v2 16/20] KVM: arm64: Simplify handling of full register invalid constraint
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[02-02 18:43]** [PATCH v2 17/20] KVM: arm64: Remove all traces of FEAT_TME
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[02-02 18:43]** [PATCH v2 18/20] KVM: arm64: Remove all traces of HCR_EL2.MIOCNCE
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[02-02 18:43]** [PATCH v2 19/20] KVM: arm64: Add sanitisation to SCTLR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[02-02 18:43]** [PATCH v2 20/20] KVM: arm64: Add debugfs file dumping computed RESx values
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[02-03 09:39]** Re: [PATCH v2 12/20] KVM: arm64: Add RES1_WHEN_E2Hx constraints as
 configuration flags
   - 发件人: Fuad Tabba <tabba@google.com>
23. **[02-03 09:41]** Re: [PATCH v2 00/20] KVM: arm64: Generalise RESx handling
   - 发件人: Fuad Tabba <tabba@google.com>
24. **[02-05 09:08]** Re: [PATCH v2 00/20] KVM: arm64: Generalise RESx handling
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [PATCH v11 00/30] Tracefs support for pKVM

**📧 邮件数**: 17 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 31 Jan 2026 13:28:18 +0000

#### 🤖 AI 总结

本邮件线程讨论的是关于为 pKVM 提供 Tracefs 支持的补丁系列（PATCH v11 00/30）。该补丁旨在增强保护模式下的调试和分析工具，Tracefs 被认为是理想的选择，因为它简单易用且支持多种工具。

在历史讨论中，Vincent Donnefort 提出了多个补丁，包括添加非消耗性读取、事件记录、简单环形缓冲区的引入、测试模块的添加以及相关文档的更新。这些补丁的目的是为 pKVM 超级管理程序提供更好的跟踪和调试能力。

本周的新讨论中，Steven Rostedt 对多个补丁进行了审查，并提出了一些具体的改进建议，例如在处理迭代器时的锁定问题以及文档的格式化。此外，他对大部分补丁给予了“Reviewed-by”标签，表明其认可。同时，Rostedt 还指出了一些测试失败的情况，并提供了修复建议，显示出补丁在测试中的进展。

总体来看，讨论集中在补丁的细节审查和改进建议上，显示出开发者对提升 pKVM 的调试能力的持续关注和努力。

#### 📝 邮件列表

1. **[01-31 13:28]** [PATCH v11 00/30] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[01-31 13:28]** [PATCH v11 07/30] tracing: Add non-consuming read to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[01-31 13:28]** [PATCH v11 09/30] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[01-31 13:28]** [PATCH v11 13/30] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[01-31 13:28]** [PATCH v11 14/30] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[01-31 13:28]** [PATCH v11 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[01-31 13:28]** [PATCH v11 16/30] Documentation: tracing: Add tracing remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[01-31 13:28]** [PATCH v11 17/30] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[02-04 17:45]** Re: [PATCH v11 00/30] Tracefs support for pKVM
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
10. **[02-04 18:52]** Re: [PATCH v11 07/30] tracing: Add non-consuming read to trace
 remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
11. **[02-04 19:40]** Re: [PATCH v11 09/30] tracing: Add events to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
12. **[02-04 20:06]** Re: [PATCH v11 13/30] tracing: Introduce simple_ring_buffer
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
13. **[02-04 20:32]** Re: [PATCH v11 14/30] tracing: Add a trace remote module for
 testing
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
14. **[02-05 12:42]** Re: [PATCH v11 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
15. **[02-05 12:45]** Re: [PATCH v11 16/30] Documentation: tracing: Add tracing remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
16. **[02-05 12:47]** Re: [PATCH v11 17/30] tracing: load/unload page callbacks for
 simple_ring_buffer
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
17. **[02-05 12:51]** Re: [PATCH v11 00/30] Tracefs support for pKVM
   - 发件人: Steven Rostedt <rostedt@goodmis.org>

---

### Thread 4: [PATCH kvmtool v5 0/7] arm64: Nested virtualization support

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 23 Jan 2026 14:27:22 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 arm64 架构的嵌套虚拟化支持的补丁（PATCH kvmtool v5 0/7），主要集中在设置维护中断（maintenance IRQ）的支持上。

**原始补丁内容**：Andre Przywara 提出的补丁系列旨在为 arm64 的嵌套虚拟化提供支持，特别是修复在某些维护中断设置失败时的边缘情况，并在未指定嵌套选项时发出警告。

**之前讨论要点**：在历史讨论中，Marc Zyngier 指出补丁存在问题，导致虚拟机无法正常工作。随后，Andre 解释了补丁中的错误，并讨论了 GICv2 和 GICv3 之间的兼容性问题。Sascha Bischoff 提出应对 GICv2 和嵌套组合的错误处理进行改进，尽管 Andre 认为这种情况并不常见，因此不需要额外的检查。

**本周新讨论**：在本周的讨论中，Andre 和 Sascha 进一步探讨了 GICv2 和 GICv3 的兼容性问题。Andre 表示不希望在 kvmtool 中进行过多的预测和过滤，认为应由内核返回错误来处理这种情况。最终，双方达成共识，认为在 EL2 模式下使用 GICv2 是一种边缘情况，因此不需要额外的显式测试。

总体来看，讨论围绕补丁的有效性和对不同中断控制器的兼容性展开，强调了在未来可能的内核更新中保持灵活性的重要性。

#### 📝 邮件列表

1. **[01-23 14:27]** [PATCH kvmtool v5 0/7] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[01-23 14:27]** [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[01-26 18:03]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting maintenance IRQ
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[01-27 12:07]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[01-27 13:23]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[01-29 18:08]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
7. **[01-30 09:29]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[02-02 09:54]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 5: [PATCH v12 0/7] support FEAT_LSUI

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 21 Jan 2026 19:06:15 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于支持 Arm 架构新特性 FEAT_LSUI 的补丁集（PATCH v12 0/7）。FEAT_LSUI 是自 Armv9.6 起引入的特性，允许特权级代码在不清除 PSTATE.PAN 位的情况下访问用户内存，从而优化了 futex 原子操作和用户交换（user_swpX）仿真。

在历史讨论中，Yeoreum Yun 提出了该补丁集的背景和必要性，详细介绍了补丁的内容，包括在 Kconfig 中添加对 LSUI 的支持（PATCH v12 1/7）以及在 CPU 特性检测中加入 FEAT_LSUI（PATCH v12 2/7）。这些补丁旨在消除使用 LSUI 指令时对 SW_PAN 处理的需求。

在本周的新讨论中，Yeoreum Yun 提醒参与者注意该补丁集的进展，Catalin Marinas 回复表示由于合并窗口即将开启，该系列补丁的优先级较低，计划在下一个周期进行处理。此外，Catalin 对 Kconfig 的位置提出了建议，认为应将其放在补丁集的最后以便于回归测试，并对补丁之间的依赖关系提出了疑虑，认为可能需要重新考虑宏的结构，以更好地支持不同的 PAN 状态。整体来看，讨论集中在补丁的优先级、结构和依赖性上。

#### 📝 邮件列表

1. **[01-21 19:06]** [PATCH v12 0/7] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[01-21 19:06]** [PATCH v12 1/7] arm64: Kconfig: add support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[01-21 19:06]** [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[02-06 09:04]** Re: [PATCH v12 0/7] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[02-06 18:35]** Re: [PATCH v12 0/7] support FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[02-06 18:36]** Re: [PATCH v12 1/7] arm64: Kconfig: add support for LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
7. **[02-06 18:42]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 6: [PATCH v1 0/3] KVM: arm64: Standardize debugfs iterators

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  2 Feb 2026 08:57:18 +0000

#### 🤖 AI 总结

本邮件讨论的主题是对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 debugfs 迭代器进行标准化的补丁系列，共包含三个补丁。

**原始问题**：现有的 debugfs 实现依赖于在全局虚拟机结构（如 `kvm_arch` 和 `vgic_dist`）中存储迭代器状态，这导致无法并发读取 debugfs 文件，并且在某些情况下可能引发引用计数泄漏。

**之前讨论要点**：历史讨论中并未涉及具体内容，但可以推测出，开发者们关注到现有实现的局限性，并计划通过标准化迭代器来解决这些问题。

**本周新讨论与进展**：
1. **补丁 1**：重构 `idregs` 的 debugfs 实现，采用标准的 `seq_file` 迭代器，解决了并发读取的问题，并消除了对 `kvm_arch` 中共享迭代器状态的依赖。
2. **补丁 2**：重新实现 `vgic-debug` 的迭代逻辑，去除了全局状态修改，采用动态迭代方式，确保了在并发修改时的安全性。
3. **补丁 3**：对 `vgic-debug` 的 debugfs 实现进行了类似的重构，采用标准的 `seq_file` 迭代器，提升了并发访问能力。

最后，Marc Zyngier 表示已将这三个补丁应用到下一个版本中，确认了补丁的有效性和必要性。

#### 📝 邮件列表

1. **[02-02 08:57]** [PATCH v1 0/3] KVM: arm64: Standardize debugfs iterators
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-02 08:57]** [PATCH v1 1/3] KVM: arm64: Use standard seq_file iterator for idregs debugfs
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[02-02 08:57]** [PATCH v1 2/3] KVM: arm64: Reimplement vgic-debug XArray iteration
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[02-02 08:57]** [PATCH v1 3/3] KVM: arm64: Use standard seq_file iterator for
 vgic-debug debugfs
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[02-05 08:57]** Re: [PATCH v1 0/3] KVM: arm64: Standardize debugfs iterators
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 7: [PATCH v3 41/47] arm_mpam: Generate a configuration for min
 controls

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 30 Jan 2026 14:17:38 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM MPAM（内存带宽分配管理）中生成最小控制配置的补丁（PATCH v3 41/47）。该补丁旨在解决在特定硬件平台（Grace）上，由于 MBW_MIN（最小内存带宽）设置不当而导致的性能问题，具体表现为 MBW_MIN 设置为 0xFFFF 时，内存带宽限制无法正常工作。

在历史讨论中，参与者指出，MBW_MIN 应该小于 MBW_MAX（最大内存带宽），并且建议将两者之间的差距设置为 5%。这项建议是为了避免在没有带宽竞争的情况下，实际带宽过于接近 MBW_MIN，从而影响性能。

在本周的新讨论中，Ben Horgan 和 Shanker Donthineni 讨论了 MBW_MIN 的默认值问题，Ben 认为将 MBW_MIN 设置为 0xFFFF 是不合理的，并提到应将其默认值改为 0。Shanker 提出了两种选择：保持当前的 5% 差距（选项A），或在未来支持 MBW_MIN 后允许用户自定义（选项B）。最终，Ben 表示倾向于选项A，以避免对现有 MBW_MAX 配置造成影响，并计划将这一政策纳入 T241-MPAM-4 的解决方案中。

总结而言，本次讨论围绕如何合理设置 MBW_MIN 和 MBW_MAX，以确保内存带宽的有效管理和性能优化展开，参与者达成了在补丁中恢复 5% 差距的共识。

#### 📝 邮件列表

1. **[01-30 14:17]** Re: [PATCH v3 41/47] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[01-30 20:30]** Re: [PATCH v3 41/47] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Shanker Donthineni <sdonthineni@nvidia.com>
3. **[02-02 10:21]** Re: [PATCH v3 41/47] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[02-02 10:34]** Re: [PATCH v3 41/47] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Shanker Donthineni <sdonthineni@nvidia.com>
5. **[02-03 09:33]** Re: [PATCH v3 41/47] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Ben Horgan <ben.horgan@arm.com>

---

### Thread 8: [PATCH 00/20] KVM: arm64: Generalise RESx handling

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 26 Jan 2026 12:16:34 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 RESx 处理的改进，特别是一个补丁系列的内容。

1. **原始 patch/问题的内容**：Marc Zyngier 提出的补丁系列旨在统一 RES0 和 RES1 位的处理，特别是针对 RES1 位的定义不清晰的问题。补丁中包括了一个新的 debugfs 文件，用于输出计算得到的 RESx 值，以便于验证和调试。

2. **之前的讨论要点**：在历史讨论中，Marc 指出当前 RESx 处理存在不一致性，特别是 RES1 位的处理依赖于临时解决方案。补丁的目标是清晰定义缺失特性时的 RES1 位，并提供统一的数据结构来管理这些位。

3. **本周的新讨论、进展或结论**：在本周的讨论中，Fuad Tabba 提出了对补丁中 debugfs 文件实现的改进建议，指出当前实现可能导致竞争条件，并建议使用无状态的 `seq_file` 实现来允许多个用户同时读取。Marc 认可了这一建议，并表示希望将 Fuad 的改进合并到当前的补丁系列中。Fuad 随后提供了相关的代码修改，进一步推动了补丁的完善。

总体来看，本周的讨论集中在如何优化 RESx 值的调试输出，确保其在多用户环境下的安全性和有效性。

#### 📝 邮件列表

1. **[01-26 12:16]** [PATCH 00/20] KVM: arm64: Generalise RESx handling
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-26 12:16]** [PATCH 20/20] KVM: arm64: Add debugfs file dumping computed RESx values
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-02 08:59]** Re: [PATCH 20/20] KVM: arm64: Add debugfs file dumping computed RESx values
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[02-02 09:14]** Re: [PATCH 20/20] KVM: arm64: Add debugfs file dumping computed RESx values
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-02 09:57]** Re: [PATCH 20/20] KVM: arm64: Add debugfs file dumping computed RESx values
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 9: [PATCH v1] KVM: arm64: nv: Use kvm_phys_size() for VNCR invalidation range

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  2 Feb 2026 13:04:24 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的一个补丁，旨在使用 `kvm_phys_size()` 函数来处理 VNCR（虚拟网络控制寄存器）失效范围的问题。

**原始补丁内容**：
补丁的主要目的是修复在使用 `pgt->ia_bits` 时可能导致的越界错误。该错误在 `kvm_nested_s2_unmap()` 和 `kvm_nested_s2_wp()` 函数中出现，原因是 `pkvm_mappings` 与 `ia_bits` 的别名关系。在 VNCR 处理代码中，使用 `kvm_phys_size()` 可以正确获取 IPA（中断地址）大小，从而避免越界问题。

**之前讨论要点**：
在之前的讨论中，参与者提到现有代码中使用 `pgt->ia_bits` 的情况并未引发类似问题，Marc Zyngier 对补丁的逻辑表示疑惑，并提出了一个替代方案，建议在进入 NV 处理代码之前检查 `kvm->arch.nested_mmus_size` 的值。

**本周的新讨论与进展**：
本周的讨论中，Fuad Tabba 和 Marc Zyngier 进行了深入交流，Marc 提出的替代方案得到了 Fuad 的认可，并表示愿意将其作为新补丁提交。两人还探讨了未来可能支持 NV 与 pkvm 的结合，显示出对该功能的进一步考虑。

总体来看，本周的讨论推动了补丁的进一步完善，并为未来的功能扩展奠定了基础。

#### 📝 邮件列表

1. **[02-02 13:04]** [PATCH v1] KVM: arm64: nv: Use kvm_phys_size() for VNCR invalidation range
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-02 14:45]** Re: [PATCH v1] KVM: arm64: nv: Use kvm_phys_size() for VNCR invalidation range
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-02 14:54]** Re: [PATCH v1] KVM: arm64: nv: Use kvm_phys_size() for VNCR
 invalidation range
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[02-02 15:04]** Re: [PATCH v1] KVM: arm64: nv: Use kvm_phys_size() for VNCR invalidation range
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH v3 02/16] KVM: arm64: nv: Implement nested Stage-2 page
 table walk logic

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 4 Feb 2026 16:28:57 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下实现嵌套 Stage-2 页表遍历逻辑的补丁（PATCH v3 02/16）。该补丁的主要目的是改进虚拟化环境中对物理地址的处理。

在历史讨论中，参与者们关注了补丁中伪代码的逻辑，指出当前代码在检查地址限制时使用了实现的物理地址（PA）大小，而不是输入地址大小（ia_size），这两者是不同的。Zenghui Yu 提出了使用 AArch64.PAMax() 函数来获取实现的 PA 大小，并建议在处理地址时应报告相应的错误。

在本周的新讨论中，Zenghui Yu 和 Marc Zyngier 继续探讨如何正确限制地址范围，讨论了是否应使用 PARange 作为限制，或者使用用户空间在虚拟机创建时定义的 IPA 范围。Marc Zyngier 还提出了修改代码的建议，以确保在读取描述符失败时能够正确报告错误代码。最终，参与者们达成了一致，认为需要进一步考虑如何在用户空间可写的 PARange 和固定的 PAMax 值之间取得平衡。

总体而言，本周的讨论深化了对补丁逻辑的理解，并推动了代码的改进方向。

#### 📝 邮件列表

1. **[02-04 16:28]** Re: [PATCH v3 02/16] KVM: arm64: nv: Implement nested Stage-2 page
 table walk logic
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
2. **[02-06 11:05]** Re: [PATCH v3 02/16] KVM: arm64: nv: Implement nested Stage-2 page table walk logic
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-09 02:34]** Re: [PATCH v3 02/16] KVM: arm64: nv: Implement nested Stage-2 page
 table walk logic
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>

---

### Thread 11: [PATCH] KVM: arm64: vgic: Handle const qualifier from clusters allocation type

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  6 Feb 2026 14:26:53 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“处理来自集群分配类型的 const 限定符”。该补丁旨在确保内存分配返回的类型与变量的类型匹配，以便为即将进行的 kmalloc 分配器类型感知做准备。

在历史讨论中，补丁的背景并未详细说明，但可以推测出，之前的实现中，内存分配器总是返回“void *”类型，这可能导致类型不匹配的问题。补丁通过使用解引用指针来确保分配的类型与“struct gic_kvm_info”完全匹配，具体修改了 vgic-init.c 文件中的一行代码。

在本周的新讨论中，Kees Cook 提出了补丁的具体实现，并在邮件中指出了修改的必要性。邮件中还提到将发送补丁的第二版（v2），表明他可能对补丁进行了进一步的调整或修正。总体来看，本周的讨论集中在补丁的实现细节和后续版本的准备上。

#### 📝 邮件列表

1. **[02-06 14:26]** [PATCH] KVM: arm64: vgic: Handle const qualifier from clusters allocation type
   - 发件人: Kees Cook <kees@kernel.org>
2. **[02-06 14:29]** Re: [PATCH] KVM: arm64: vgic: Handle const qualifier from clusters
 allocation type
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 12: [PATCH kvmtool v2 00/17] arm64: Support GICv5-based guests

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 5 Feb 2026 10:58:11 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于支持基于 GICv5 的 arm64 客户机的补丁系列（[PATCH kvmtool v2 00/17]）。该补丁旨在增强 kvmtool，使其能够更好地支持 GICv5 相关的功能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁系列是基于之前的 NV 系列进行开发的，涉及对 GICv5 的支持和相关的功能更新。

在本周的新讨论中，参与者 Fuad Tabba 表达了对该补丁系列的审查和测试兴趣，并询问了补丁的存放位置。Sascha Bischoff 随后提供了补丁的存储链接，并指出了最新版本的变化，包括在帮助信息中添加了关于 GICv5 和 GICv5-ITS 的说明。他还提到，为了避免与用户 API 的不匹配，使用者应仅应用到特定的补丁。此外，Sascha 还分享了其他相关的 KVM 改动和运行 GICv5 的指导链接。

总体来看，本周的讨论主要集中在补丁的审查、测试以及相关资源的共享上，推动了 GICv5 支持的进一步发展。

#### 📝 邮件列表

1. **[02-05 10:58]** Re: [PATCH kvmtool v2 00/17] arm64: Support GICv5-based guests
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-05 18:23]** Re: [PATCH kvmtool v2 00/17] arm64: Support GICv5-based guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 13: [PATCH v1] KVM: arm64: nv: Avoid NV stage-2 code when NV is not supported

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  2 Feb 2026 15:22:53 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（内核虚拟机）在 arm64 架构下的补丁，旨在避免在不支持嵌套虚拟化（NV）的情况下调用 NV 的阶段2 代码。

**原始补丁内容**：
补丁的主要目的是在虚拟机未分配任何嵌套 MMU（内存管理单元）的情况下，防止进入 NV 处理函数。具体来说，补丁通过在相关函数中添加检查，确保只有在 `kvm->arch.nested_mmus_size` 大于零时才执行 NV 相关操作，以避免在保护 KVM（pKVM）环境中出现的越界错误。

**之前讨论要点**：
在历史讨论中没有提供具体的背景信息，但补丁的提出是为了修复在处理嵌套虚拟化时可能引发的 UBSAN（未定义行为检测器）错误，确保系统的稳定性和安全性。

**本周的新讨论与进展**：
本周的讨论中，Fuad Tabba 提交了补丁，并详细解释了其功能和必要性。Marc Zyngier 随后确认已将该补丁应用到下一个版本中，表示感谢并结束了讨论。这表明补丁得到了认可并将被纳入后续的内核版本中。

#### 📝 邮件列表

1. **[02-02 15:22]** [PATCH v1] KVM: arm64: nv: Avoid NV stage-2 code when NV is not supported
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-02 15:47]** Re: [PATCH v1] KVM: arm64: nv: Avoid NV stage-2 code when NV is not supported
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH v2] KVM: arm64: vgic: Handle const qualifier from gic_kvm_info allocation type

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  6 Feb 2026 14:30:23 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic（虚拟通用中断控制器）模块的一个补丁。补丁的主要内容是处理 gic_kvm_info 分配类型中的 const 限定符，以确保分配的返回类型与被赋值的变量类型匹配。

在历史讨论中并未提供相关背景信息，因此我们只能聚焦于本周的新讨论。Kees Cook 提出的补丁旨在为即将进行的 kmalloc 分配器类型感知做准备。之前，分配器总是返回 "void *" 类型，这可以隐式转换为任何指针类型。当前的分配类型是 "struct gic_kvm_info"，但返回的类型是带有 const 限定符的。为了解决这个不匹配问题，补丁建议使用解引用指针来获取正确的大小。

本周的讨论中，Kees Cook 提交了补丁并进行了相应的代码修改，确保在 vgic_set_kvm_info 函数中，gic_kvm_info 的分配与其类型完全匹配。补丁已在代码中进行了相应的插入和删除操作，以实现这一目标。

#### 📝 邮件列表

1. **[02-06 14:30]** [PATCH v2] KVM: arm64: vgic: Handle const qualifier from gic_kvm_info allocation type
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 15: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu property

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 6 Feb 2026 14:59:14 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM KVM 的补丁，具体内容是增加一个名为 `kvm-psci-version` 的虚拟 CPU 属性。该属性用于设置 KVM 提供给虚拟机的电源状态协调接口（PSCI）固件 ABI 版本，默认情况下，KVM 将使用其已知的最新版本（在 Linux v6.13 中为 PSCI v1.3）。用户需要设置此属性的原因是为了能够将虚拟机迁移到运行旧内核的主机上，这些旧内核可能不识别默认的 PSCI 版本。

在之前的讨论中，参与者对该补丁表示认可，并提到需要更详细的描述和一些编码风格的建议，比如结构体名称应使用 CamelCase 风格，以及使用 `ARRAY_SIZE()` 来设置循环边界。此外，讨论中还提到可以考虑将 PSCI 版本以人类可读的形式呈现，而不是十六进制表示。

本周的讨论主要集中在补丁的细节和编码风格的建议上，参与者 Peter Maydell 提出了对补丁的认可，并表示在其他设计讨论未完全解决的情况下，可以接受该补丁的提交。他的反馈包括对错误报告的建议，强调在迁移过程中用户可能遇到的问题及其解决方案。总体来看，补丁得到了积极的反馈，并有望尽快合并。

#### 📝 邮件列表

1. **[02-06 14:59]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>

---

### Thread 16: [PATCH v9 01/30] arm64/sysreg: Update SMIDR_EL1 to DDI0601 2025-06

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 03 Feb 2026 13:00:27 +0000

#### 🤖 AI 总结

本邮件主题为“[PATCH v9 01/30] arm64/sysreg: Update SMIDR_EL1 to DDI0601 2025-06”，涉及对 ARM64 架构中 SMIDR_EL1 寄存器的更新，目的是将其更新至 DDI0601 版本，预计在 2025 年 6 月发布。

在历史讨论中，尚未提供具体的背景信息或前期讨论内容，因此我们无法了解该补丁的详细背景或之前的争论点。

在本周的新讨论中，参与者 Mark Brown 对该补丁进行了审核，并表示已通过审核（Reviewed-by），由 Alex Bennée 进行确认。这表明该补丁得到了积极的反馈，可能即将进入下一步的处理阶段。

总体而言，本周的讨论主要集中在对补丁的审核上，显示出该补丁在社区中的认可度。

#### 📝 邮件列表

1. **[02-03 13:00]** Re: [PATCH v9 01/30] arm64/sysreg: Update SMIDR_EL1 to DDI0601 2025-06
   - 发件人: =?utf-8?Q?Alex_Benn=C3=A9e?= <alex.bennee@linaro.org>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 updates for 7.0

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  6 Feb 2026 15:33:45 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM/arm64 在 7.0 版本中的更新。Marc Zyngier 提交了一个初步的更新集，主要分为两个类别：一是针对 pKVM 的修复，确保不应暴露给客户机或主机的特性确实被隔离；二是对寄存器清理基础设施的重构，包括对新寄存器的清理。

在之前的讨论中，未提供具体的历史背景信息，因此无法总结相关的历史讨论要点。

本周的新讨论中，Marc Zyngier 提供了详细的更新内容，包括对 FEAT_IDST 的支持，使未实现的 ID 寄存器能够正常报告为陷阱而非未定义异常；对 VTCR_EL2 寄存器的清理，修复了一些 UXN/PXN/XN 的错误；以及对 RESx 位的全面处理，增加了 SCTLR_EL2 到清理寄存器列表中。此外，还包含了多项针对 pKVM 的修复，确保主机禁用 MTE 时不会对虚拟机造成攻击风险。其他更新还包括调试和自测的修复，以及一些低影响的改动和拼写修正。

总之，本周的更新为 KVM/arm64 的稳定性和安全性提供了重要改进。

#### 📝 邮件列表

1. **[02-06 15:33]** [GIT PULL] KVM/arm64 updates for 7.0
   - 发件人: Marc Zyngier <maz@kernel.org>

---

