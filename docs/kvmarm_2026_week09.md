# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2026-03-02 00:29:53

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 271
- **总 Thread 数**: 32
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 26 threads (237 邮件)
- **RFC**: 1 threads (1 邮件)
- **Bug Report**: 1 threads (3 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Discussion**: 1 threads (2 邮件)
- **Other**: 2 threads (26 邮件)

---

## 📌 PATCH

共 26 个 thread

---

### Thread 1: [PATCH v5 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code

**📧 邮件数**: 53 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 24 Feb 2026 17:56:39 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM MPAM（内存分区和监控）与 resctrl（资源控制）结合的补丁系列，主要内容如下：

1. **原始补丁内容**：补丁系列的主要目标是将 MPAM 的功能与 resctrl 结合，使其能够在用户空间中使用。补丁包括对 MPAM 控制和监控的支持，特别是针对 ARM64 架构的 KVM（虚拟化）支持。

2. **历史讨论要点**：之前的讨论集中在 MPAM 的实现细节上，包括如何处理 CPU 资源的分配、监控和错误处理等。参与者们讨论了如何确保 MPAM 的功能能够有效地与 resctrl 交互，并解决了在不同硬件平台上可能遇到的兼容性问题。

3. **本周新讨论和进展**：本周的讨论主要集中在补丁的具体实现和测试反馈上。参与者们对补丁进行了测试，并提出了一些建议和改进意见，包括对特定硬件缺陷的处理（如 T241-MPAM 的工作区）。此外，补丁还引入了对 MPAM 监控的初始化和域管理的支持。最后，补丁系列得到了多个参与者的审核和认可，预计将合并到主线中。

总的来说，本邮件线程展示了 ARM MPAM 与 resctrl 结合的技术细节和实现进展，强调了社区协作在解决复杂问题中的重要性。

#### 📝 邮件列表

1. **[02-24 17:56]** [PATCH v5 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[02-24 17:56]** [PATCH v5 01/41] arm64/sysreg: Add MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[02-24 17:56]** [PATCH v5 02/41] KVM: arm64: Preserve host MPAM configuration when changing traps
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[02-24 17:56]** [PATCH v5 03/41] KVM: arm64: Make MPAMSM_EL1 accesses UNDEF
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[02-24 17:56]** [PATCH v5 04/41] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[02-24 17:56]** [PATCH v5 05/41] arm64: mpam: Re-initialise MPAM regs when CPU comes online
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[02-24 17:56]** [PATCH v5 06/41] arm64: mpam: Drop the CONFIG_EXPERT restriction
   - 发件人: Ben Horgan <ben.horgan@arm.com>
8. **[02-24 17:56]** [PATCH v5 07/41] arm64: mpam: Advertise the CPUs MPAM limits to the driver
   - 发件人: Ben Horgan <ben.horgan@arm.com>
9. **[02-24 17:56]** [PATCH v5 08/41] arm64: mpam: Add cpu_pm notifier to restore MPAM sysregs
   - 发件人: Ben Horgan <ben.horgan@arm.com>
10. **[02-24 17:56]** [PATCH v5 09/41] arm64: mpam: Initialise and context switch the MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
11. **[02-24 17:56]** [PATCH v5 10/41] arm64: mpam: Add helpers to change a task or cpu's MPAM PARTID/PMG values
   - 发件人: Ben Horgan <ben.horgan@arm.com>
12. **[02-24 17:56]** [PATCH v5 11/41] KVM: arm64: Force guest EL1 to use user-space's partid configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
13. **[02-24 17:56]** [PATCH v5 12/41] KVM: arm64: Use kernel-space partid configuration for hypercalls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
14. **[02-24 17:56]** [PATCH v5 13/41] arm_mpam: resctrl: Add boilerplate cpuhp and domain allocation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[02-24 17:56]** [PATCH v5 14/41] arm_mpam: resctrl: Pick the caches we will use as resctrl resources
   - 发件人: Ben Horgan <ben.horgan@arm.com>
16. **[02-24 17:56]** [PATCH v5 15/41] arm_mpam: resctrl: Implement resctrl_arch_reset_all_ctrls()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
17. **[02-24 17:56]** [PATCH v5 16/41] arm_mpam: resctrl: Add resctrl_arch_get_config()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
18. **[02-24 17:56]** [PATCH v5 17/41] arm_mpam: resctrl: Implement helpers to update configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
19. **[02-24 17:56]** [PATCH v5 18/41] arm_mpam: resctrl: Add plumbing against arm64 task and cpu hooks
   - 发件人: Ben Horgan <ben.horgan@arm.com>
20. **[02-24 17:56]** [PATCH v5 19/41] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
21. **[02-24 17:56]** [PATCH v5 20/41] arm_mpam: resctrl: Convert to/from MPAMs fixed-point formats
   - 发件人: Ben Horgan <ben.horgan@arm.com>
22. **[02-24 17:57]** [PATCH v5 21/41] arm_mpam: resctrl: Add kunit test for control format conversions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
23. **[02-24 17:57]** [PATCH v5 22/41] arm_mpam: resctrl: Add rmid index helpers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
24. **[02-24 17:57]** [PATCH v5 23/41] arm_mpam: resctrl: Add kunit test for rmid idx conversions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
25. **[02-24 17:57]** [PATCH v5 24/41] arm_mpam: resctrl: Wait for cacheinfo to be ready
   - 发件人: Ben Horgan <ben.horgan@arm.com>
26. **[02-24 17:57]** [PATCH v5 25/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
27. **[02-24 17:57]** [PATCH v5 26/41] arm_mpam: resctrl: Add monitor initialisation and domain boilerplate
   - 发件人: Ben Horgan <ben.horgan@arm.com>
28. **[02-24 17:57]** [PATCH v5 27/41] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
29. **[02-24 17:57]** [PATCH v5 28/41] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
30. **[02-24 17:57]** [PATCH v5 29/41] arm_mpam: resctrl: Pre-allocate free running monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
31. **[02-24 17:57]** [PATCH v5 30/41] arm_mpam: resctrl: Allow resctrl to allocate monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
32. **[02-24 17:57]** [PATCH v5 31/41] arm_mpam: resctrl: Add resctrl_arch_rmid_read() and resctrl_arch_reset_rmid()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
33. **[02-24 17:57]** [PATCH v5 32/41] arm_mpam: resctrl: Update the rmid reallocation limit
   - 发件人: Ben Horgan <ben.horgan@arm.com>
34. **[02-24 17:57]** [PATCH v5 33/41] arm_mpam: resctrl: Add empty definitions for assorted resctrl functions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
35. **[02-24 17:57]** [PATCH v5 34/41] arm64: mpam: Select ARCH_HAS_CPU_RESCTRL
   - 发件人: Ben Horgan <ben.horgan@arm.com>
36. **[02-24 17:57]** [PATCH v5 35/41] arm_mpam: resctrl: Call resctrl_init() on platforms that can support resctrl
   - 发件人: Ben Horgan <ben.horgan@arm.com>
37. **[02-24 17:57]** [PATCH v5 36/41] arm_mpam: Add quirk framework
   - 发件人: Ben Horgan <ben.horgan@arm.com>
38. **[02-24 17:57]** [PATCH v5 37/41] arm_mpam: Add workaround for T241-MPAM-1
   - 发件人: Ben Horgan <ben.horgan@arm.com>
39. **[02-24 17:57]** [PATCH v5 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
40. **[02-24 17:57]** [PATCH v5 39/41] arm_mpam: Add workaround for T241-MPAM-6
   - 发件人: Ben Horgan <ben.horgan@arm.com>
41. **[02-24 17:57]** [PATCH v5 40/41] arm_mpam: Quirk CMN-650's CSU NRDY behaviour
   - 发件人: Ben Horgan <ben.horgan@arm.com>
42. **[02-24 17:57]** [PATCH v5 41/41] arm64: mpam: Add initial MPAM documentation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
43. **[02-25 14:25]** Re: [PATCH v5 19/41] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Zeng Heng <zengheng4@huawei.com>
44. **[02-25 11:01]** Re: [PATCH v5 41/41] arm64: mpam: Add initial MPAM documentation
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
45. **[02-25 11:03]** Re: [PATCH v5 15/41] arm_mpam: resctrl: Implement
 resctrl_arch_reset_all_ctrls()
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
46. **[02-25 11:14]** Re: [PATCH v5 26/41] arm_mpam: resctrl: Add monitor initialisation
 and domain boilerplate
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
47. **[02-25 21:10]** Re: [PATCH v5 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
48. **[02-26 11:47]** Re: [PATCH v5 26/41] arm_mpam: resctrl: Add monitor initialisation
 and domain boilerplate
   - 发件人: Zeng Heng <zengheng4@huawei.com>
49. **[02-26 15:34]** Re: [PATCH v5 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Zeng Heng <zengheng4@huawei.com>
50. **[02-26 10:26]** Re: [PATCH v5 26/41] arm_mpam: resctrl: Add monitor initialisation
 and domain boilerplate
   - 发件人: Ben Horgan <ben.horgan@arm.com>
51. **[02-27 11:01]** Re: [PATCH v5 26/41] arm_mpam: resctrl: Add monitor initialisation
 and domain boilerplate
   - 发件人: Zeng Heng <zengheng4@huawei.com>
52. **[02-27 17:04]** Re: [PATCH v5 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
53. **[03-01 09:28]** Re: [PATCH v5 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Fenghua Yu <fenghuay@nvidia.com>

---

### Thread 2: [PATCH v5 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support

**📧 邮件数**: 37 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 26 Feb 2026 15:55:21 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 KVM（内核虚拟机）在 arm64 架构下引入虚拟 GICv5（vgic_v5）及其 PPI（私有中断）支持的补丁系列（PATCH v5 00/36）。以下是讨论的主要内容：

1. **原始补丁内容**：该补丁系列的目标是实现虚拟 GICv5 设备的支持，初步只支持 PPI，后续将添加对 SPI 和 LPI 的支持。补丁中对 GICv5 的实现进行了多项改进，包括分离主机能力与客户配置、更新中断处理程序、以及对系统寄存器的清理等。

2. **历史讨论要点**：在之前的讨论中，补丁的不同版本（v1 到 v4）已被多次审查和修改，主要集中在如何更好地支持 GICv5 的功能，以及如何确保向后兼容性，特别是与现有 GICv3 系统的兼容性。

3. **本周的新讨论和进展**：
   - 本周的讨论主要集中在补丁的具体实现细节上，包括对 PPI 中断的直接注入、对 GICv5 寄存器的访问控制、以及如何处理用户空间对 PPI 的驱动请求等。
   - 还讨论了如何在 GICv5 环境中处理定时器中断，确保在进入和退出虚拟机时正确管理中断状态。
   - 另外，补丁中引入了新的用户 API，以允许用户空间查询可驱动的 PPI 列表。
   - 最后，针对 GICv5 的自测代码也被添加，以确保新功能的正确性。

总的来说，本次邮件讨论展示了 KVM 在支持 GICv5 方面的持续进展，强调了与用户空间交互的必要性，以及如何在虚拟化环境中有效管理中断。

#### 📝 邮件列表

1. **[02-26 15:55]** [PATCH v5 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[02-26 15:55]** [PATCH v5 01/36] KVM: arm64: vgic-v3: Drop userspace write
 sanitization for ID_AA64PFR0.GIC on GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[02-26 15:55]** [PATCH v5 02/36] KVM: arm64: vgic: Rework vgic_is_v3() and add
 vgic_host_has_gicvX()
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[02-26 15:56]** [PATCH v5 03/36] KVM: arm64: Return early from
 kvm_finalize_sys_regs() if guest has run
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[02-26 15:56]** [PATCH v5 04/36] arm64/sysreg: Add remaining GICv5 ICC_ & ICH_
 sysregs for KVM support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[02-26 15:56]** [PATCH v5 05/36] arm64/sysreg: Add GICR CDNMIA encoding
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[02-26 15:56]** [PATCH v5 06/36] KVM: arm64: gic-v5: Add ARM_VGIC_V5 device to KVM
 headers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[02-26 15:57]** [PATCH v5 07/36] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
9. **[02-26 15:57]** [PATCH v5 08/36] KVM: arm64: gic-v5: Add Arm copyright header
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[02-26 15:57]** [PATCH v5 09/36] KVM: arm64: gic-v5: Detect implemented PPIs on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
11. **[02-26 15:58]** [PATCH v5 10/36] KVM: arm64: gic-v5: Sanitize ID_AA64PFR2_EL1.GCIE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[02-26 15:58]** [PATCH v5 11/36] KVM: arm64: gic-v5: Support GICv5 FGTs & FGUs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[02-26 15:58]** [PATCH v5 12/36] KVM: arm64: gic-v5: Add emulation for
 ICC_IAFFIDR_EL1 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[02-26 15:58]** [PATCH v5 13/36] KVM: arm64: gic-v5: Trap and emulate ICC_IDR0_EL1
 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[02-26 15:59]** [PATCH v5 14/36] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp
 interface
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
16. **[02-26 15:59]** [PATCH v5 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[02-26 15:59]** [PATCH v5 16/36] KVM: arm64: gic-v5: Implement direct injection of
 PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
18. **[02-26 15:59]** [PATCH v5 17/36] KVM: arm64: gic-v5: Finalize GICv5 PPIs and generate
 mask
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
19. **[02-26 16:00]** [PATCH v5 18/36] KVM: arm64: gic: Introduce queue_irq_unlock to
 irq_ops
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
20. **[02-26 16:00]** [PATCH v5 19/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
21. **[02-26 16:00]** [PATCH v5 20/36] KVM: arm64: gic-v5: Init Private IRQs (PPIs) for
 GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
22. **[02-26 16:00]** [PATCH v5 21/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
23. **[02-26 16:01]** [PATCH v5 22/36] KVM: arm64: gic-v5: Trap and mask guest
 ICC_PPI_ENABLERx_EL1 writes
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
24. **[02-26 16:01]** [PATCH v5 23/36] KVM: arm64: gic-v5: Support GICv5 interrupts with
 KVM_IRQ_LINE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
25. **[02-26 16:01]** [PATCH v5 24/36] KVM: arm64: gic-v5: Create and initialise vgic_v5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
26. **[02-26 16:01]** [PATCH v5 25/36] KVM: arm64: gic-v5: Initialise ID and priority bits
 when resetting vcpu
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
27. **[02-26 16:02]** [PATCH v5 26/36] KVM: arm64: gic-v5: Enlighten arch timer for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
28. **[02-26 16:02]** [PATCH v5 27/36] KVM: arm64: gic-v5: Mandate architected PPI for PMU
 emulation on GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
29. **[02-26 16:02]** [PATCH v5 28/36] KVM: arm64: gic: Hide GICv5 for protected guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
30. **[02-26 16:02]** [PATCH v5 29/36] KVM: arm64: gic-v5: Hide FEAT_GCIE from NV GICv5
 guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
31. **[02-26 16:03]** [PATCH v5 30/36] KVM: arm64: gic-v5: Introduce kvm_arm_vgic_v5_ops
 and register them
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
32. **[02-26 16:03]** [PATCH v5 31/36] KVM: arm64: gic-v5: Set ICH_VCTLR_EL2.En on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
33. **[02-26 16:03]** [PATCH v5 32/36] KVM: arm64: gic-v5: Probe for GICv5 device
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
34. **[02-26 16:04]** [PATCH v5 33/36] Documentation: KVM: Introduce documentation for
 VGICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
35. **[02-26 16:04]** [PATCH v5 34/36] KVM: arm64: selftests: Introduce a minimal GICv5 PPI
 selftest
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
36. **[02-26 16:04]** [PATCH v5 35/36] KVM: arm64: gic-v5: Communicate userspace-driveable
 PPIs via a UAPI
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
37. **[02-26 16:04]** [PATCH v5 36/36] KVM: arm64: selftests: Add no-vgic-v5 selftest
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 3: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context

**📧 邮件数**: 18 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 16 Feb 2026 13:09:59 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 KVM 的 arm64 架构中禁用 TRBE（Trace Buffer Unit）在虚拟机上下文中运行的问题。最初的补丁（patch）由 Will Deacon 提出，目的是在虚拟机上下文中禁用 TRBE，以防止在使用自托管 TRBE 的主机中产生不必要的跟踪数据。历史讨论中，参与者们探讨了 TRBE 的设计缺陷以及其在异常处理中的不可靠性，认为在当前架构下，TRBE 无法有效支持虚拟机的跟踪需求。

在本周的新讨论中，Marc Zyngier 和 Leo Yan 强调了 TRBE 在处理虚拟机生成的异常时的局限性，指出如果无法遵循架构的保证，就无法实现有效的跟踪。同时，Leo Yan 提出了一个补充建议，认为在 KVM 上下文切换时不需要禁用和重新启用 TRCPRGCTLR.EN 位，因为在切换回主机时，跟踪单元能够保证连续的跟踪流。讨论中还提到了一些锁定问题，Leo Yan 提出了一个补丁系列来解决这些问题。

总体来看，邮件讨论围绕 TRBE 的设计缺陷、在虚拟化环境中的应用限制，以及如何改进当前实现以确保跟踪数据的有效性展开。

#### 📝 邮件列表

1. **[02-16 13:09]** [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Will Deacon <will@kernel.org>
2. **[02-16 14:29]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-16 15:05]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
4. **[02-16 15:51]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-16 16:10]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
6. **[02-16 16:49]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-16 18:14]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
8. **[02-17 14:19]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
9. **[02-17 14:52]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
10. **[02-17 19:01]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
11. **[02-19 13:54]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
12. **[02-19 18:58]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
13. **[02-20 11:42]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
14. **[02-20 15:48]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
15. **[02-24 11:19]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[02-24 11:22]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[02-25 12:09]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
18. **[02-27 18:07]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 4: [PATCH v14 0/8] support FEAT_LSUI

**📧 邮件数**: 17 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 25 Feb 2026 18:27:00 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM 架构的补丁集，主题为支持 FEAT_LSUI（Unprivileged Load Store Instructions）。该补丁集的主要目的是在不清除 PSTATE.PAN 位的情况下，允许特权级别的代码访问用户内存，特别是在 futex 原子操作中应用这一特性。

历史讨论中，补丁经历了多个版本的迭代，逐步完善了功能，包括添加 CPU 特性检测、修复构建错误、简化代码等。补丁集的版本更新从 v1 到 v14，逐步引入了对 FEAT_LSUI 的支持，并在 KVM 中暴露给虚拟机。

在本周的新讨论中，Yeoreum Yun 提出了多个补丁，涵盖了对 FEAT_LSUI 的支持，包括：
1. 在 CPU 特性中添加 FEAT_LSUI 的检测。
2. 在 KVM 中向虚拟机暴露 FEAT_LSUI。
3. 为 FEAT_LSUI 添加测试覆盖。
4. 重构 futex 原子操作以支持 FEAT_LSUI。
5. 禁用 SWP 指令的仿真，以消除 PAN 切换。
6. 使用 CASLT 指令来交换虚拟机描述符。

参与者对补丁进行了审查和讨论，提出了一些改进建议，包括将某些代码块移动到更合适的位置，以提高补丁的可读性和逻辑性。整体来看，本周的讨论集中在补丁的细节调整和代码优化上，确保 FEAT_LSUI 的实现更加稳健。

#### 📝 邮件列表

1. **[02-25 18:27]** [PATCH v14 0/8] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[02-25 18:27]** [PATCH v14 1/8] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[02-25 18:27]** [PATCH v14 2/8] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[02-25 18:27]** [PATCH v14 3/8] KVM: arm64: kselftest: set_id_regs: add test for FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[02-25 18:27]** [PATCH v14 4/8] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[02-25 18:27]** [PATCH v14 5/8] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[02-25 18:27]** [PATCH v14 6/8] arm64: armv8_deprecated: disable swp emulation when FEAT_LSUI present
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[02-25 18:27]** [PATCH v14 7/8] KVM: arm64: use CASLT instruction for swapping guest descriptor
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[02-25 18:27]** [PATCH v14 8/8] arm64: Kconfig: add support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[02-26 11:16]** Re: [PATCH v14 7/8] KVM: arm64: use CASLT instruction for swapping guest descriptor
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-26 11:28]** Re: [PATCH v14 7/8] KVM: arm64: use CASLT instruction for swapping
 guest descriptor
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
12. **[02-26 03:38]** Re: [PATCH v14 7/8] KVM: arm64: use CASLT instruction for swapping
 guest descriptor
   - 发件人: Oliver Upton <oupton@kernel.org>
13. **[02-26 13:52]** Re: [PATCH v14 7/8] KVM: arm64: use CASLT instruction for swapping
 guest descriptor
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
14. **[02-26 13:53]** Re: [PATCH v14 7/8] KVM: arm64: use CASLT instruction for swapping
 guest descriptor
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
15. **[02-26 14:05]** Re: [PATCH v14 7/8] KVM: arm64: use CASLT instruction for swapping
 guest descriptor
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
16. **[02-26 14:52]** Re: [PATCH v14 7/8] KVM: arm64: use CASLT instruction for swapping
 guest descriptor
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
17. **[02-27 08:31]** Re: [PATCH v14 7/8] KVM: arm64: use CASLT instruction for swapping
 guest descriptor
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 5: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource

**📧 邮件数**: 14 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 13 Feb 2026 15:38:09 +0800

#### 🤖 AI 总结

在本次邮件讨论中，主要围绕「[PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource」的补丁进行。该补丁旨在为ARM架构的MPAM（内存性能监控和管理）驱动添加对内存带宽（MB）资源的支持。

**历史讨论要点**：
1. 之前的讨论中提到，现有的MPAM驱动在某些系统上对MB控制的支持有限，特别是当MPAM内存类MSC位于内存控制器而非L3缓存时，MB控制和带宽监控无法启用。
2. Zeng Heng和Ben Horgan等参与者对MPAM功能进行了测试，确认了L2和L3的CPBM（缓存性能监控）等功能正常，但MB功能尚未支持，原因在于驱动未能识别MATA（内存控制器）模块。

**本周新讨论进展**：
1. Zeng Heng进一步阐述了MATA的功能及其在Kunpeng平台上的应用，指出MB相关的MSC位于MATA模块中，导致当前驱动无法提供支持。
2. Ben Horgan对Zeng的测试结果表示感谢，并提出了调试建议，要求共享更多的调试信息以帮助解决问题。
3. Zeng Heng确认在最新的v5版本中，MSC初始化的重构可能意外修复了L2初始化错误，且在最新测试中未再出现之前的错误信息。

总体来看，讨论围绕如何增强MPAM驱动的功能展开，尤其是在支持MB资源方面，参与者们积极分享测试结果和调试信息，以推动补丁的完善和功能的实现。

#### 📝 邮件列表

1. **[02-13 15:38]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Zeng Heng <zengheng4@huawei.com>
2. **[02-14 17:40]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Zeng Heng <zengheng4@huawei.com>
3. **[02-14 18:39]** Re: [PATCH v4 18/41] arm_mpam: resctrl: Implement helpers to update
 configuration
   - 发件人: Zeng Heng <zengheng4@huawei.com>
4. **[02-16 12:22]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[02-16 13:54]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[02-16 14:23]** Re: [PATCH v4 18/41] arm_mpam: resctrl: Implement helpers to update
 configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[02-18 16:22]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
8. **[02-24 19:03]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Zeng Heng <zengheng4@huawei.com>
9. **[02-24 14:19]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
10. **[02-24 15:27]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
11. **[02-24 17:53]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
12. **[02-25 14:39]** Re: [PATCH v4 18/41] arm_mpam: resctrl: Implement helpers to update
 configuration
   - 发件人: Zeng Heng <zengheng4@huawei.com>
13. **[02-25 16:08]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Zeng Heng <zengheng4@huawei.com>
14. **[02-26 15:17]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Zeng Heng <zengheng4@huawei.com>

---

### Thread 6: [PATCH v13 0/8] support FEAT_LSUI

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 23 Feb 2026 17:47:54 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[PATCH v13 0/8] support FEAT_LSUI”的补丁集，旨在支持Armv9.6引入的FEAT_LSUI特性，该特性允许特权级代码在不清除PSTATE.PAN位的情况下访问用户内存。

在历史讨论中，补丁经历了多个版本的迭代，从v1到v13，主要改动包括重构原子操作、添加对LSUI的支持、以及在KVM中暴露该特性给虚拟机。补丁集的核心是通过LSUI指令优化futex原子操作，减少对PAN位的切换。

本周的新讨论中，Yeoreum Yun提交了8个补丁，涵盖了对KVM的支持、futex操作的重构、以及对LSUI的测试覆盖等。补丁得到了Marc Zyngier和Catalin Marinas的审核与认可。此外，Oliver Upton提出了在Kconfig检查中应使用cpucap_is_possible()的建议，Yeoreum表示会进行修正。

总体而言，本周的讨论集中在补丁的细节完善和功能验证上，推动了LSUI特性的集成进程。

#### 📝 邮件列表

1. **[02-23 17:47]** [PATCH v13 0/8] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[02-23 17:47]** [PATCH v13 1/8] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[02-23 17:47]** [PATCH v13 2/8] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[02-23 17:47]** [PATCH v13 3/8] KVM: arm64: kselftest: set_id_regs: add test for FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[02-23 17:47]** [PATCH v13 4/8] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[02-23 17:47]** [PATCH v13 5/8] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[02-23 17:48]** [PATCH v13 6/8] arm64: armv8_deprecated: disable swp emulation when FEAT_LSUI present
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[02-23 17:48]** [PATCH v13 7/8] KVM: arm64: use CASLT instruction for swapping guest descriptor
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[02-23 17:48]** [PATCH v13 8/8] arm64: Kconfig: add support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[02-24 12:54]** Re: [PATCH v13 7/8] KVM: arm64: use CASLT instruction for swapping
 guest descriptor
   - 发件人: Oliver Upton <oupton@kernel.org>
11. **[02-25 17:10]** Re: [PATCH v13 7/8] KVM: arm64: use CASLT instruction for swapping
 guest descriptor
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 7: [PATCH v15 0/8] support FEAT_LSUI

**📧 邮件数**: 9 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Feb 2026 15:16:57 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个名为“支持 FEAT_LSUI”的补丁集（PATCH v15 0/8），该补丁旨在为 Armv9.6 引入的 FEAT_LSUI 特性提供支持。FEAT_LSUI 允许特权级代码在不清除 PSTATE.PAN 位的情况下访问用户内存，从而简化了内存访问的处理。

在历史讨论中，补丁经历了多个版本的迭代，主要集中在代码的清理、功能的增强以及对不同编译器的兼容性修复。例如，从 v14 到 v15 的更新中，修正了拼写错误并进行了代码清理，之前版本则增加了对 LSUI 的配置检查和 clang 编译器的支持。

本周的新讨论中，Yeoreum Yun 提交了八个补丁，涵盖了以下关键内容：
1. **补丁 1**：添加 FEAT_LSUI 的 CPU 特性检测，确保在支持 FEAT_PAN 的情况下启用 LSUI。
2. **补丁 2**：将 FEAT_LSUI 暴露给虚拟机（KVM）。
3. **补丁 3**：为 FEAT_LSUI 添加测试覆盖。
4. **补丁 4**：重构 futex 原子操作以支持 LSUI。
5. **补丁 5**：实现使用 LSUI 的 futex 原子操作。
6. **补丁 6**：在支持 LSUI 的情况下禁用 SWP 指令的仿真。
7. **补丁 7**：使用 CAST 指令交换虚拟机描述符，避免清除 PAN 位。
8. **补丁 8**：在 Kconfig 中添加 LSUI 的支持选项。

这些补丁的提交得到了相关开发者的认可，标志着对 FEAT_LSUI 支持的进一步完善。

#### 📝 邮件列表

1. **[02-27 15:16]** [PATCH v15 0/8] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[02-27 15:16]** [PATCH v15 1/8] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[02-27 15:16]** [PATCH v15 2/8] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[02-27 15:17]** [PATCH v15 3/8] KVM: arm64: kselftest: set_id_regs: add test for FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[02-27 15:17]** [PATCH v15 4/8] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[02-27 15:17]** [PATCH v15 5/8] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[02-27 15:17]** [PATCH v15 6/8] arm64: armv8_deprecated: disable swp emulation when FEAT_LSUI present
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[02-27 15:17]** [PATCH v15 7/8] KVM: arm64: use CAST instruction for swapping guest descriptor
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[02-27 15:17]** [PATCH v15 8/8] arm64: Kconfig: add support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 8: [PATCH v3 0/5] Support the FEAT_HDBSS introduced in Armv9.5

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Feb 2026 12:04:16 +0800

#### 🤖 AI 总结

本邮件线程讨论了对 ARMv9.5 中引入的硬件脏状态跟踪结构（HDBSS）特性的支持，包含五个补丁的更新。

1. **原始补丁内容**：该补丁系列旨在实现 HDBSS 特性，利用硬件支持来跟踪内存页的脏状态，从而减少在虚拟机迁移过程中的开销。用户可以通过 `KVM_CAP_ARM_HW_DIRTY_STATE_TRACK` ioctl 接口启用或禁用该特性。

2. **之前讨论要点**：在之前的讨论中，参与者们探讨了 HDBSS 的实现细节，包括如何处理内存访问异常、DBM（脏位修改器）属性的设置，以及如何在虚拟机迁移时有效地记录脏页。讨论还涉及了是否需要用户空间显式启用 HDBSS 的问题。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的具体实现和接口设计上。参与者提出了将 HDBSS 自动启用的建议，以简化用户空间的操作流程，并讨论了在迁移开始时动态分配 HDBSS 缓冲区的可能性。此外，针对补丁中的一些定义和功能，参与者们提出了优化建议，如确保内存对齐和简化不必要的定义。最终，开发者表示将在下一版本中整合这些反馈，进一步优化补丁内容。

整体来看，本周的讨论推动了 HDBSS 特性在 KVM 中的实现进展，并为后续版本的改进奠定了基础。

#### 📝 邮件列表

1. **[02-25 12:04]** [PATCH v3 0/5] Support the FEAT_HDBSS introduced in Armv9.5
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
2. **[02-25 12:04]** [PATCH v3 1/5] arm64/sysreg: Add HDBSS related register information
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
3. **[02-25 12:04]** [PATCH v3 2/5] KVM: arm64: Add support to set the DBM attr during memory abort
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
4. **[02-25 12:04]** [PATCH v3 3/5] KVM: arm64: Add support for FEAT_HDBSS
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
5. **[02-25 12:04]** [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
6. **[02-25 12:04]** [PATCH v3 5/5] KVM: arm64: Document HDBSS ioctl
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
7. **[02-25 17:46]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Leonardo Bras <leo.bras@arm.com>
8. **[02-27 18:47]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF
 events
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
9. **[02-27 14:10]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Leonardo Bras <leo.bras@arm.com>

---

### Thread 9: [PATCH 0/9] arm64: Fully disable configured-out features

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 19 Feb 2026 19:55:23 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构中完全禁用已配置特性的补丁（PATCH 0/9）。最初的补丁由 Marc Zyngier 提出，主要针对在禁用 FEAT_S1POE 支持时，硬件仍然暴露该特性的问题。这可能导致内核中不同部分对特性的认知不一致，从而引发状态泄漏。补丁的目标是确保在特性被禁用时，相关信息不会在内核的其他部分可见。

在历史讨论中，参与者们探讨了如何有效地从清理后的 ID 寄存器中完全移除特性，并讨论了不同特性（如 Pointer Auth、SVE 等）的处理方式。Fuad Tabba 提出了对补丁的优化建议，包括结构体的内存布局和条件处理的安全性。

在本周的新讨论中，Marc Zyngier 和 Suzuki K Poulose 继续围绕补丁进行交流，确认了对特性处理的建议，并提出了将特性设置函数封装的想法，以提高代码的可读性和可维护性。整体来看，讨论进展顺利，参与者们对补丁的方向表示认可，并提出了进一步的改进建议。

#### 📝 邮件列表

1. **[02-19 19:55]** [PATCH 0/9] arm64: Fully disable configured-out features
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-19 19:55]** [PATCH 1/9] arm64: Add logic to fully remove features from sanitised id registers
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-20 08:36]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from
 sanitised id registers
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[02-20 10:09]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from sanitised id registers
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-20 11:06]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from
 sanitised id registers
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[02-20 14:52]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from sanitised id registers
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-20 15:36]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from
 sanitised id registers
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[02-23 09:48]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from sanitised id registers
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-23 18:18]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from
 sanitised id registers
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 10: [PATCH v3 0/2] KVM: arm64: PMU: Use multiple host PMUs

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Feb 2026 13:31:14 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的性能监控单元（PMU）支持多个主机 PMU 的补丁。原始补丁（PATCH v3 0/2）旨在解决在异构 arm64 系统中，vCPU 迁移到不兼容的物理 CPU 时，PMU 计数器停止递增的问题。这种情况在 Windows 客户端中可能导致崩溃。当前的解决方法要求虚拟机监控器（VMM）将 vCPU 固定到共享兼容 PMU 的物理 CPU，但这在 QEMU/libvirt 中实现起来较为复杂。

补丁引入了 `KVM_ARM_VCPU_PMU_V3_FIXED_COUNTERS_ONLY` 属性，允许 KVM 在没有可编程事件计数器的情况下模拟 PMUv3，从而使 Windows 客户端能够在异构系统上可靠运行，而无需进行 vCPU 固定。这一补丁的更新版本（v3）对属性进行了重命名，并添加了在加载 vCPU 时创建性能计数器的请求。

本周的讨论中，参与者 Akihiko Odaki 提出了补丁的具体实现细节，并进行了自测，确保新属性的功能正常。Oliver Upton 提出了对补丁的改进建议，包括将迁移处理整合到现有的 PMU 重新加载函数中，以简化代码结构。双方讨论了如何在不影响性能的情况下优化代码，并确保虚拟机在迁移时能够正确处理 PMU 事件。

总的来说，本周的讨论集中在补丁的实现细节和代码优化上，参与者们对如何更好地处理 PMU 迁移和事件调度进行了深入交流。

#### 📝 邮件列表

1. **[02-25 13:31]** [PATCH v3 0/2] KVM: arm64: PMU: Use multiple host PMUs
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
2. **[02-25 13:31]** [PATCH v3 1/2] KVM: arm64: PMU: Introduce FIXED_COUNTERS_ONLY
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
3. **[02-25 13:31]** [PATCH v3 2/2] KVM: arm64: selftests: Test
 PMU_V3_FIXED_COUNTERS_ONLY
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
4. **[02-26 03:54]** Re: [PATCH v3 1/2] KVM: arm64: PMU: Introduce FIXED_COUNTERS_ONLY
   - 发件人: Oliver Upton <oupton@kernel.org>
5. **[02-26 23:43]** Re: [PATCH v3 1/2] KVM: arm64: PMU: Introduce FIXED_COUNTERS_ONLY
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
6. **[02-26 23:47]** Re: [PATCH v3 1/2] KVM: arm64: PMU: Introduce FIXED_COUNTERS_ONLY
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
7. **[02-26 15:05]** Re: [PATCH v3 1/2] KVM: arm64: PMU: Introduce FIXED_COUNTERS_ONLY
   - 发件人: Oliver Upton <oupton@kernel.org>
8. **[02-27 18:34]** Re: [PATCH v3 1/2] KVM: arm64: PMU: Introduce FIXED_COUNTERS_ONLY
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>

---

### Thread 11: [PATCH 0/2] arm64/mm: Drop TTBR_CNP_BIT and TTBR_ASID_MASK

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Feb 2026 03:51:23 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 ARM64 架构内存管理的两个补丁，主要涉及去除冗余的宏定义 TTBR_CNP_BIT 和 TTBR_ASID_MASK，直接使用标准的工具 sysreg 格式字段宏 TTBRx_EL1_CNP_BIT 和 TTBRx_EL1_ASID_MASK。

在历史讨论中，Anshuman Khandual 提出了这两个补丁，目的是简化代码，消除不再需要的自定义宏。之前的讨论中，已经有人建议采用这种做法，以提高代码的可读性和一致性。

在本周的新讨论中，Anshuman Khandual 提交了补丁的具体实现，并指出这些更改不会引入功能性变化。Marc Zyngier 对补丁提出了建议，建议在某些构造中使用 FIELD_PREP() 函数，以提高代码的清晰度。Anshuman 随后表示同意，并计划根据建议进行修改。

总体而言，本周的讨论集中在补丁的具体实现和代码优化建议上，推动了 ARM64 内存管理代码的改进。

#### 📝 邮件列表

1. **[02-25 03:51]** [PATCH 0/2] arm64/mm: Drop TTBR_CNP_BIT and TTBR_ASID_MASK
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-25 03:51]** [PATCH 0/2] arm64/mm: Drop TTBR_CNP_BIT and TTBR_ASID_MASK
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-25 03:51]** [PATCH 1/2] arm64/mm: Directly use TTBRx_EL1_ASID_MASK
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[02-25 03:51]** [PATCH 2/2] arm64/mm: Directly use TTBRx_EL1_CnP
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[02-25 09:23]** Re: [PATCH 1/2] arm64/mm: Directly use TTBRx_EL1_ASID_MASK
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-25 16:10]** Re: [PATCH 1/2] arm64/mm: Directly use TTBRx_EL1_ASID_MASK
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
7. **[02-25 10:50]** Re: [PATCH 1/2] arm64/mm: Directly use TTBRx_EL1_ASID_MASK
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 13 Feb 2026 14:16:19 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 `__delay()` 函数中强制使用 `CNTVCT_EL0` 的补丁（patch）。该补丁的背景是，Hyesoo Yu 报告了在 KVM 不处于 VHE 模式时，`__delay()` 使用 `WFxT` 时出现的问题，导致使用虚拟计数器而非物理计数器，从而引发潜在的计时错误。

在历史讨论中，Marc Zyngier 提出了补丁的初步版本，并指出了问题的核心，即在某些情况下，`__delay()` 读取计数器的方式不当，可能导致不一致的行为。

在本周的新讨论中，Ben Horgan 提到在运行 7.0-rc1 时出现了 `CONFIG_DEBUG_PREEMPT` 警告，并提出了一个解决方案，但 Marc Zyngier 认为这种做法可能会隐藏问题，建议保留对预先中断的禁用，以确保在非故障系统中能够正确读取计数器。随后，Will Deacon 也参与讨论，指出实现这些工作绕过的复杂性，并提出了对补丁的进一步改进建议。

总体而言，本周的讨论集中在如何正确实现补丁以避免潜在的计时错误，并确保在不同 CPU 状态下的稳定性。参与者们对补丁的实现细节进行了深入探讨，尚未达成最终结论。

#### 📝 邮件列表

1. **[02-13 14:16]** [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-23 11:16]** Re: [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[02-23 14:31]** Re: [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-23 15:14]** Re: [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[02-25 22:36]** Re: [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()
   - 发件人: Will Deacon <will@kernel.org>
6. **[02-26 08:16]** Re: [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 9 Feb 2026 18:57:06 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM64 架构中添加 CPU 特性 FEAT_LSUI 的补丁（PATCH v12 2/7）。该补丁的目的是在 CPU 特性中引入 FEAT_LSUI，以支持相关的功能。

在历史讨论中，参与者探讨了 FEAT_LSUI 与 FEAT_PAN 之间的依赖关系。Catalin Marinas 提到，由于在 7.0 版本中移除了 CONFIG_ARM64_PAN，导致禁用该特性变得更加困难。Yeoreum Yun 则对 FEAT_PAN 的必要性提出了疑问，认为在没有 FEAT_PAN 的硬件上启用 FEAT_LSUI 可能是不合理的。讨论中还提到，虚拟化可能导致某些硬件组合出现不一致的情况。

在本周的新讨论中，Yeoreum Yun 提出了一个建议，即在处理 LSUI 时，使用 uaccess_ttbr0_enable() 而不是在 uaccess_enable_privileged() 中进行特殊处理，以保持一致性。这一建议得到了 Catalin 的认可，认为这样做更符合逻辑。

总体来看，讨论围绕 FEAT_LSUI 的实现细节及其与其他特性的兼容性展开，参与者们达成了一些共识，并提出了改进建议。

#### 📝 邮件列表

1. **[02-09 18:57]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[02-10 09:54]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[02-10 16:14]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[02-10 17:01]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[02-16 18:24]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[02-23 15:54]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 14: [PATCH v2 0/3] KVM: arm64: Fix SPE and TRBE nVHE world switch

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Feb 2026 21:21:32 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM (Kernel-based Virtual Machine) 在 arm64 架构下的 nVHE (Non-Virtual Hypervisor Extension) 世界切换过程中，修复 SPE (Statistical Profiling Extension) 和 TRBE (Trace Buffer Extension) 的相关问题。Will Deacon 提出了三个补丁（patch），旨在解决在虚拟机上下文中运行时可能导致的错误。

首先，补丁的内容包括：
1. 禁用在来宾上下文中运行时的 TRBE 追踪缓冲区；
2. 禁用在来宾上下文中运行时的 SPE 统计分析缓冲区；
3. 在 BRBE（Branch Record Buffer Extension）世界切换例程中不再传递 host_debug_state。

在历史讨论中，补丁 v1 版本已被提出，但存在一些问题，如缺少内存屏障和对 CPU 错误的处理。Will 在 v2 版本中进行了改进，增加了必要的内存屏障和注释，并解决了已知的 CPU 错误。

本周的新讨论中，Will 详细解释了每个补丁的实现细节，强调了在 nVHE 世界切换时，确保 TRBE 和 SPE 不会在来宾上下文中启用的重要性，以防止数据损坏和硬件锁死。此外，他指出了对 CPU errata 的处理，确保补丁的稳定性和可靠性。整体来看，本周的讨论集中在补丁的具体实现和潜在影响上，推动了该问题的解决进程。

#### 📝 邮件列表

1. **[02-27 21:21]** [PATCH v2 0/3] KVM: arm64: Fix SPE and TRBE nVHE world switch
   - 发件人: Will Deacon <will@kernel.org>
2. **[02-27 21:21]** [PATCH v2 1/3] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Will Deacon <will@kernel.org>
3. **[02-27 21:21]** [PATCH v2 2/3] KVM: arm64: Disable SPE Profiling Buffer when running in guest context
   - 发件人: Will Deacon <will@kernel.org>
4. **[02-27 21:21]** [PATCH v2 3/3] KVM: arm64: Don't pass host_debug_state to BRBE world-switch routines
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 15: [PATCH 0/3] KVM: arm64: minor fixes about S2 page table walker

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 26 Feb 2026 01:35:12 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 S2 页表遍历器的几个小修复。

1. **原始 patch/问题的内容**：
   本次讨论包含三个补丁，旨在修复 S2 页表遍历过程中的一些问题。补丁内容涉及检查 S2 限制、报告地址大小故障以及在无法读取描述符时注入 SEA（Synchronous Exception Acknowledgment）。

2. **之前讨论要点**：
   之前的讨论主要集中在如何正确实现嵌套的 S2 页表遍历逻辑，特别是确保在不同的物理地址范围下，页表的有效性检查能够正确执行。相关的补丁在此基础上进行了一些小的修正。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Zenghui Yu 提出了三个补丁：
   - 第一个补丁修正了 S2 限制检查的逻辑，使其基于实现的物理地址大小进行验证。
   - 第二个补丁确保在 TTBR_ELx（Translation Table Base Register）配置错误时，报告的地址大小故障级别为 0。
   - 第三个补丁则在读取描述符失败时注入 SEA，以确保虚拟机的稳定性。

这些修复将提升 KVM 在处理嵌套页表时的准确性和可靠性。

#### 📝 邮件列表

1. **[02-26 01:35]** [PATCH 0/3] KVM: arm64: minor fixes about S2 page table walker
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
2. **[02-26 01:35]** [PATCH 1/3] KVM: arm64: nv: Check S2 limits based on implemented PA size
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
3. **[02-26 01:35]** [PATCH 2/3] KVM: arm64: nv: Report addrsz fault at level 0 with a bad VTTBR.BADDR
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
4. **[02-26 01:35]** [PATCH 3/3] KVM: arm64: nv: Inject a SEA if failed to read the descriptor
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>

---

### Thread 16: [PATCH v6 0/1] arm: add kvm-psci-version vcpu property

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 20 Feb 2026 12:56:55 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM 架构的 KVM 的补丁，旨在添加一个名为 `kvm-psci-version` 的虚拟 CPU 属性，以便请求特定的 PSCI 版本。这一补丁的主要目的是支持在不同默认 PSCI 版本的主机内核之间进行迁移。

在历史讨论中，Sebastian Ott 提出了这个补丁，并指出为了支持 PSCI v0.1，需要放弃使用 `KVM_CAP_ARM_PSCI_0_2` 进行的虚拟 CPU 初始化。此外，补丁中列出了当前支持的 PSCI 版本，包括 0.1、0.2、1.0、1.1、1.2 和 1.3，并得到了 Eric Auger 的审查和测试支持。

在本周的新讨论中，Peter Maydell 提出了一个关于补丁中数据类型的问题，指出 `%hd` 是一个有符号值，可能会接受不合适的输入，建议使用 `%hu`。Sebastian Ott 认可了这一建议，并表示将会在本地进行修正，而不需要重新提交补丁。这表明讨论的氛围积极，参与者之间的沟通顺畅。

#### 📝 邮件列表

1. **[02-20 12:56]** [PATCH v6 0/1] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[02-20 12:56]** [PATCH v6 1/1] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[02-24 14:34]** Re: [PATCH v6 1/1] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
4. **[02-25 08:16]** Re: [PATCH v6 1/1] target/arm/kvm: add kvm-psci-version vcpu
 property
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 17: [PATCH v2] KVM: arm64: vgic: Handle const qualifier from gic_kvm_info allocation type

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 13 Feb 2026 15:03:24 +0000

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH v2] KVM: arm64: vgic: 处理来自 gic_kvm_info 分配类型的 const 限定符”。该补丁旨在解决在 KVM 的 ARM64 虚拟化环境中，处理 GIC（通用中断控制器）信息时的 const 限定符问题。

在历史讨论中，Kees Cook 提交了该补丁，并得到了 Marc Zyngier 的确认，Marc 表示已将该补丁应用于修复集，并感谢 Kees 的贡献。补丁的提交标识为 ee5c38a8d31e5dea52299c43c2ec3213351ab6e1。

在本周的新讨论中，Marc Zyngier 更新了补丁的进展，表示已将其发送给 Linus 以便纳入 -rc1 版本，并提醒 Kees 可能会导致合并冲突。Kees Cook 随后回应，表示在准备 KVM/arm64 的修复时注意到了这一点，并希望未来能提前了解补丁的处理路线，以便更好地协调，避免与上游的冲突。

总体来看，本周的讨论主要集中在补丁的进展和未来沟通的建议上。

#### 📝 邮件列表

1. **[02-13 15:03]** Re: [PATCH v2] KVM: arm64: vgic: Handle const qualifier from gic_kvm_info allocation type
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-25 12:40]** Re: [PATCH v2] KVM: arm64: vgic: Handle const qualifier from
 gic_kvm_info allocation type
   - 发件人: Kees Cook <kees@kernel.org>
3. **[02-25 21:10]** Re: [PATCH v2] KVM: arm64: vgic: Handle const qualifier from gic_kvm_info allocation type
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH v6 00/19] ARM64 PMU Partitioning

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 25 Feb 2026 17:40:55 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 ARM64 PMU（性能监控单元）分区的补丁系列（PATCH v6 00/19）。该补丁旨在改进 ARM64 架构下的 PMU 功能，特别是在虚拟化环境中的表现。

在历史讨论中，尽管没有具体的邮件记录，但可以推测该补丁系列涉及对 PMU 的分区管理，以便更好地支持 KVM（内核虚拟机）环境下的性能监控。

本周的新讨论中，参与者 Colton Lewis 和 Marc Zyngier 进行了几轮交流。Colton 提到他已经向相关人员发送了补丁以进行审查，并在讨论中提到他会尝试完整退出以验证某些功能的有效性。此外，Colton 还发现自己在补丁中引入了一个错误，原本应该使用位或（|）而不是位与（&），并向邮件列表通报了这一问题，以便其他人可以尝试运行他的补丁系列。

总体来看，本周的讨论集中在补丁的审查和错误修正上，显示出开发者们对改进 ARM64 PMU 功能的持续关注和合作。

#### 📝 邮件列表

1. **[02-25 17:40]** Re: [PATCH v6 00/19] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[02-25 17:45]** Re: [PATCH v6 09/19] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[02-25 17:53]** Re: [PATCH v6 06/19] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

### Thread 19: [PATCH] KVM: arm64: Deduplicate ASID retrieval code

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 25 Feb 2026 10:47:18 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在去重 ASID（地址空间标识符）检索代码。补丁的主要内容是将现有的三种 ASID 检索实现合并为一种通用的实现，并在此过程中简化代码，使用 TTBRx_EL1_ASID 宏。

在历史讨论中，补丁的背景并未详细阐述，但可以推测出之前的实现存在重复代码的问题，影响了代码的可维护性和清晰性。

本周的新讨论中，Marc Zyngier 提出了补丁并详细描述了其功能，随后得到了参与者 Jonathan Cameron 和 Joey Gouly 的审查与认可，均表示补丁符合预期并给予了“Reviewed-by”的反馈。这表明补丁在社区中得到了积极的响应，可能会在后续的版本中被合并进主线代码。整体来看，本周的讨论集中在补丁的审查与确认上，未出现新的争议或问题。

#### 📝 邮件列表

1. **[02-25 10:47]** [PATCH] KVM: arm64: Deduplicate ASID retrieval code
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-25 11:24]** Re: [PATCH] KVM: arm64: Deduplicate ASID retrieval code
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
3. **[02-25 11:35]** Re: [PATCH] KVM: arm64: Deduplicate ASID retrieval code
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 20: [PATCH] irqchip/gic-v5: Fix inversion of IRS_IDR0.virt flag

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Feb 2026 08:31:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 GICv5 中 IRS_IDR0.virt 标志反转问题的修复补丁。原始补丁由 Sascha Bischoff 提出，目的是修复在检测主机 GICv5 实现是否具备虚拟化能力时，逻辑反转的问题。具体来说，代码中的逻辑运算符在清理过程中被错误地修改，导致虚拟化能力的检测结果不正确。补丁通过重新添加缺失的逻辑运算符来修复这一行为。

在之前的讨论中，Sascha Bischoff 提到这个问题是由于过于积极的代码清理导致的，并对此表示歉意。Marc Zyngier 也对此进行了确认，并表示将把这个修复纳入下一批 KVM 修复中。

本周的新进展是，Marc Zyngier 确认已将该补丁应用于修复列表，并感谢 Sascha 的贡献。补丁的提交记录为 29c8b85adb47daefc213381bc1831787f512d89b，标志着问题的解决。

#### 📝 邮件列表

1. **[02-25 08:31]** [PATCH] irqchip/gic-v5: Fix inversion of IRS_IDR0.virt flag
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[02-25 08:52]** Re: [PATCH] irqchip/gic-v5: Fix inversion of IRS_IDR0.virt flag
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-25 08:58]** Re: [PATCH] irqchip/gic-v5: Fix inversion of IRS_IDR0.virt flag
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH v1] KVM: arm64: Revert accidental drop of kvm_uninit_stage2_mmu()
 for non-NV VMs

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Sun, 22 Feb 2026 08:33:52 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的一个补丁，目的是恢复对非 NV（非嵌套虚拟机）环境中 `kvm_uninit_stage2_mmu()` 的调用。历史讨论中，Fuad Tabba 提到，之前的提交（commit 0c4762e26879）为了防止在访问非嵌套虚拟机的页面表时出现越界错误，意外地在多个函数中添加了早期返回，这导致 `kvm_arch_flush_shadow_all()` 跳过了对 `kvm_uninit_stage2_mmu(kvm)` 的调用，从而影响了 pKVM 的正常工作。

在本周的新讨论中，Mark Brown 对补丁进行了测试，确认其解决了之前在使用 qemu 运行 kselftests 时出现的一些偶发性内存不足（OOM）问题，并表示感谢。Marc Zyngier 则表示已将该补丁应用到修复列表中，确认了补丁的有效性。

总结来看，此次补丁的恢复不仅修复了功能缺失问题，还改善了系统的稳定性。

#### 📝 邮件列表

1. **[02-22 08:33]** [PATCH v1] KVM: arm64: Revert accidental drop of kvm_uninit_stage2_mmu()
 for non-NV VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-23 16:16]** Re: [PATCH v1] KVM: arm64: Revert accidental drop of
 kvm_uninit_stage2_mmu() for non-NV VMs
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[02-23 16:31]** Re: [PATCH v1] KVM: arm64: Revert accidental drop of kvm_uninit_stage2_mmu() for non-NV VMs
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 22: [PATCH] KVM: arm64: Fix protected mode handling of pages larger than 4kB

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 22 Feb 2026 14:10:00 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM 在处理大于 4KB 页时的保护模式问题。历史讨论中，Marc Zyngier 提出了一个补丁（patch），该补丁旨在解决自从引入了对 pKVM 映射的跟踪后，非 4KB 页支持完全失效的问题，导致虚拟机无法启动。具体问题表现为系统不断出现相同的故障，无法向前推进。

在本周的新讨论中，Marc Zyngier 确认已将该补丁应用于修复中，并感谢参与者的贡献。补丁的提交标识为 08f97454b7fa39bfcf82524955c771d2d693d6fe，表明问题已得到解决。

总结而言，历史讨论中指出了 KVM 在处理大页时的严重问题，而本周的进展则是确认补丁已成功应用，问题得到修复。

#### 📝 邮件列表

1. **[02-22 14:10]** [PATCH] KVM: arm64: Fix protected mode handling of pages larger than 4kB
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-23 16:31]** Re: [PATCH] KVM: arm64: Fix protected mode handling of pages larger than 4kB
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 23: [PATCH] KVM: arm64: Eagerly init vgic dist/redist on vgic creation

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 28 Feb 2026 16:45:59 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 ARM64 架构下的 VGIC（虚拟通用中断控制器）初始化问题。Marc Zyngier 提出的补丁旨在解决在 VGIC 创建过程中，如果 `vgic_allocate_private_irqs_locked()` 函数失败，可能导致 `dist->rd_regions` 未初始化的问题。这种情况会在后续的 `kvm_vgic_dist_destroy()` 函数中引发错误，导致无法正确释放资源。

在历史讨论中，补丁的背景未详细列出，但可以推测出之前的讨论涉及 VGIC 的初始化过程及其在错误处理方面的不足。本周的讨论中，Marc Zyngier 提出了具体的解决方案：通过提前进行静态初始化，确保在失败时能够合理地进行资源清理。此外，他还建议在失败时重置 VGIC 模型，以防止潜在的错误。

本周的进展主要是补丁的具体实现，包括对 `vgic_create()` 函数的修改，以提高其健壮性和错误处理能力。补丁已由测试工具 syzbot 进行验证，确保其有效性。

#### 📝 邮件列表

1. **[02-28 16:45]** [PATCH] KVM: arm64: Eagerly init vgic dist/redist on vgic creation
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 24: [PATCH v3 15/15] KVM: arm64: selftests: Add test for AT emulation

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 28 Feb 2026 17:43:59 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试，特别是针对 AT（Access Type）仿真功能的测试。原始的 patch 提出了增加一个测试用例，以验证 AT 仿真在不同情况下的表现。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出该 patch 的目的是为了增强 KVM 的稳定性和可靠性，确保其在处理访问类型时能够正确地进行错误处理和故障检测。

在本周的新讨论中，参与者 Zenghui Yu 对 Oliver Upton 提出的观点进行了回应，分享了他在 QEMU 环境中测试该 patch 的结果。他指出，在执行测试时，遇到了阶段 2 的翻译故障，导致测试失败。具体来说，测试中预期的故障并没有如预期发生，反而触发了不同的行为，这使得他对是否能够强制 KVM 使用“慢速” AT 仿真路径产生了疑问。

总的来说，本周的讨论集中在测试结果的分析上，揭示了当前 patch 在实际应用中的一些潜在问题，并对 KVM 的 AT 仿真路径的行为提出了进一步的思考。

#### 📝 邮件列表

1. **[02-28 17:43]** Re: [PATCH v3 15/15] KVM: arm64: selftests: Add test for AT emulation
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>

---

### Thread 25: [PATCH v2] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU
 tables

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 25 Feb 2026 17:29:05 +0530

#### 🤖 AI 总结

本邮件主题为“[PATCH v2] KVM: arm64: nv: 优化 shadow S2-MMU 表的反向映射”，主要讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的优化补丁。

1. **原始 patch/问题的内容**：该补丁旨在优化反向映射 shadow S2-MMU 表，以提高性能和效率。

2. **之前讨论要点**：由于本邮件线程没有历史讨论记录，因此没有相关的背景信息或之前的讨论要点。

3. **本周的新讨论、进展或结论**：本周的讨论由 Vishnu Pajjuri 发起，他表示在 Ganapatrao Kulkarni 离开 Ampere 后，开始跟进该补丁的进展，并请求 Marc 的指导，询问是否有推荐的建议或替代步骤。这表明该补丁仍在积极推进中，且需要进一步的技术指导。

总结来看，本周的讨论主要集中在对补丁的后续跟进和寻求建议上，显示出对优化工作的持续关注。

#### 📝 邮件列表

1. **[02-25 17:29]** Re: [PATCH v2] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU
 tables
   - 发件人: Vishnu Pajjuri <vishnu@os.amperecomputing.com>

---

### Thread 26: [PATCH v9 00/30] KVM: arm64: Implement support for SME

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 25 Feb 2026 09:22:36 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中实现对 ARM64 架构的 SME（Scalable Matrix Extension）支持的补丁（PATCH v9 00/30）。该补丁旨在增强 KVM 对 ARM64 处理器新特性的支持，以提升虚拟化性能和功能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了响应 ARM64 处理器架构的最新发展，尤其是与 SME 相关的功能需求。

本周的新讨论中，参与者 Alex Bennée 提到 Richard Henderson 发布了一个初步的 QEMU RFC（请求反馈）系列，旨在为 KVM 支持 SME 提供测试基础。该 RFC 包含 13 个补丁，旨在实现对 SME 的支持，并鼓励开发者进行测试。此外，建议在 kvm-unit-tests 中添加一些 SME2 工作负载，以便更好地验证和测试该功能，类似于 GIC ITS 迁移的测试方式。

总的来说，本周的讨论主要集中在如何通过 QEMU 测试和验证新补丁的有效性，以及对 SME2 工作负载的建议。

#### 📝 邮件列表

1. **[02-25 09:22]** Re: [PATCH v9 00/30] KVM: arm64: Implement support for SME
   - 发件人: =?utf-8?Q?Alex_Benn=C3=A9e?= <alex.bennee@linaro.org>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH] arm: enable PMU partitioning

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 25 Feb 2026 17:37:32 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM 主机上启用 PMU（性能监控单元）分区的 RFC Patch。该补丁的主要内容是设置 vCPU 设备属性，以在 ARM 主机上无条件启用 PMU 分区功能。补丁的实验性特征在于，如果调用失败，程序会立即中止。为了使调用成功，主机必须运行支持 ARM64 PMU 分区特性的内核，并在内核命令行中设置相应参数。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测该主题可能涉及对 ARM 架构中 PMU 功能的扩展和改进，尤其是在虚拟化环境中的应用。

本周的新讨论中，补丁的作者 Colton Lewis 提供了详细的实现细节，包括对多个文件的修改，增加了 PMU 分区的设置函数，并在相应的头文件中定义了新的属性。这些变更旨在为 ARM CPU 提供更好的性能监控能力，尤其是在虚拟化场景下。整体来看，本周的进展主要集中在补丁的具体实现和功能验证上。

#### 📝 邮件列表

1. **[02-25 17:37]** [RFC PATCH] arm: enable PMU partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: [syzbot] [kvmarm?] [kvm?] BUG: unable to handle kernel paging request
 in kvm_vgic_destroy

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 28 Feb 2026 03:46:20 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM (Kernel-based Virtual Machine) 的内核错误，具体是在 `kvm_vgic_destroy` 函数中出现的内核分页请求处理问题。该问题由 syzbot 发现，报告显示在特定的内核提交（6316366129d2）中，系统在处理虚拟地址时发生了错误，导致内核崩溃。

在历史讨论中，虽然没有具体的历史邮件，但本周的讨论中，Marc Zyngier 提到该问题可能是由于在 `vgic_allocate_private_irqs_locked()` 函数失败后，未能正确初始化 `dist->rd_regions`，导致后续的 `kvm_vgic_dist_destroy()` 函数出现问题。他建议改进测试用例，以确保在调试文件系统不可用时能及时停止测试。

本周的新进展包括，Marc 提出了一个修复补丁，并在邮件中提供了测试指令。syzbot 随后测试了该补丁，结果显示修复成功，未再触发原有问题。测试结果表明，修复有效，且没有应用其他补丁。

#### 📝 邮件列表

1. **[02-28 03:46]** [syzbot] [kvmarm?] [kvm?] BUG: unable to handle kernel paging request
 in kvm_vgic_destroy
   - 发件人: syzbot <syzbot+f6a46b038fc243ac0175@syzkaller.appspotmail.com>
2. **[02-28 14:55]** Re: [syzbot] [kvmarm?] [kvm?] BUG: unable to handle kernel paging request in kvm_vgic_destroy
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-28 07:57]** Re: [syzbot] [kvmarm?] [kvm?] BUG: unable to handle kernel paging
 request in kvm_vgic_destroy
   - 发件人: syzbot <syzbot+f6a46b038fc243ac0175@syzkaller.appspotmail.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 7.0, take #1

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Feb 2026 10:50:47 +0000

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 7.0 版本中的修复补丁。Marc Zyngier 提交了第一批修复，主要集中在 pKVM 的功能集和 MMU 方面，同时也包括 GICv5 的修复和一些小的代码清理。补丁的主要内容包括确保在支持 S1POE 的硬件上，来宾之间不会泄露 S1POE 状态；将主机的 ID 寄存器传递给非保护的 pKVM 虚拟机；修复处理大于 4KB 页面时的对齐问题等。

在之前的讨论中，未提及具体的历史背景，但可以看出这些修复是针对 KVM/arm64 的一系列问题，旨在提升系统的稳定性和安全性。

本周的新进展是，Marc Zyngier 提交的补丁已被 Paolo Bonzini 成功拉取，表示感谢。这表明这些修复已被接受并将纳入后续的开发中。整体来看，这些修复将有助于改善 KVM/arm64 的性能和可靠性。

#### 📝 邮件列表

1. **[02-26 10:50]** [GIT PULL] KVM/arm64 fixes for 7.0, take #1
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-28 16:04]** Re: [GIT PULL] KVM/arm64 fixes for 7.0, take #1
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Discussion

共 1 个 thread

---

### Thread 1: [kvmtool PATCH v5 02/15] update_headers: arm64: Track psci.h for
 PSCI definitions

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 9 Feb 2026 15:51:37 +0000

#### 🤖 AI 总结

在本次邮件讨论中，主题为更新 KVM 工具中 ARM64 架构的 PSCI 定义相关头文件的补丁（patch）。历史讨论中，Suzuki K Poulose 提到当前没有 arm64 的 `uapi/asm/psci.h` 文件，建议使用 `linux/psci.h`，并表示将自行更新头文件以满足其他需求。Will Deacon 同意这一观点，并决定先应用第一个补丁。

在本周的新讨论中，Suzuki K Poulose 对 Will Deacon 的反馈表示关注，指出 `psci.h` 确实存在于通用的用户空间 API（uapi）中，并承诺在下一个补丁版本中修正此问题。此外，他建议在工具脚本中添加警告信息，以便在缺少头文件时能够及时捕捉到错误。

总结来看，讨论主要围绕如何正确引用和更新 PSCI 相关头文件展开，参与者们对补丁的适用性和后续改进达成了一致意见。

#### 📝 邮件列表

1. **[02-09 15:51]** Re: [kvmtool PATCH v5 02/15] update_headers: arm64: Track psci.h for
 PSCI definitions
   - 发件人: Will Deacon <will@kernel.org>
2. **[02-27 10:23]** Re: [kvmtool PATCH v5 02/15] update_headers: arm64: Track psci.h for
 PSCI definitions
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [kvmtool PATCH v6 00/17] kvmtool: arm64: Handle PSCI calls in userspace

**📧 邮件数**: 18 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Feb 2026 16:56:07 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 工具的第六版补丁系列，主要集中在 ARM64 架构下的 PSCI 调用处理。补丁的核心内容是实现用户空间对 PSCI 调用的支持，利用 SMCCC 过滤能力来处理这些调用。

在历史讨论中，补丁的前几个版本（v4 和 v5）主要集中在更新头文件、修复构建错误以及清理代码等方面。参与者们讨论了如何将 PSCI 调用的处理从内核转移到用户空间，以提高灵活性和可维护性。

本周的新讨论中，补丁的具体实现逐步完善，包括：
1. 实现了 PSCI 的基本功能，如 CPU_SUSPEND、CPU_ON、AFFINITY_INFO、MIGRATE_INFO_TYPE 和 SYSTEM_{OFF,RESET} 等。
2. 增加了对 PSCI 调用的用户空间转发支持，确保符合 PSCI 1.0 规范。
3. 通过 ioctl 调用管理 vCPU 的状态，确保在执行 PSCI 调用时，能够正确处理 CPU 的电源状态和重置操作。

总的来说，这一系列补丁为 KVM 工具在 ARM64 架构下提供了更强大的功能，允许用户空间直接处理 PSCI 调用，提升了虚拟化的能力和效率。

#### 📝 邮件列表

1. **[02-27 16:56]** [kvmtool PATCH v6 00/17] kvmtool: arm64: Handle PSCI calls in userspace
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
2. **[02-27 16:56]** [kvmtool PATCH v6 01/17] util/update_headers: Update linux/const.h from linux sources
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
3. **[02-27 16:56]** [kvmtool PATCH v6 02/17] util/update_headers: Clean up header copying
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
4. **[02-27 16:56]** [kvmtool PATCH v6 03/17] util/update_headers: Warn about missing header files
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
5. **[02-27 16:56]** [kvmtool PATCH v6 04/17] update_headers: arm64: Track uapi/linux/psci.h for PSCI definitions
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
6. **[02-27 16:56]** [kvmtool PATCH v6 05/17] arm64: Sync headers from Linux v6.19 for psci.h
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
7. **[02-27 16:56]** [kvmtool PATCH v6 06/17] Import arm-smccc.h from Linux v6.19
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[02-27 16:56]** [kvmtool PATCH v6 07/17] arm64: Stash kvm_vcpu_init for later use
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
9. **[02-27 16:56]** [kvmtool PATCH v6 08/17] arm64: Use KVM_SET_MP_STATE ioctl to power off non-boot vCPUs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
10. **[02-27 16:56]** [kvmtool PATCH v6 09/17] arm64: Expose ARM64_CORE_REG() for general use
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
11. **[02-27 16:56]** [kvmtool PATCH v6 10/17] arm64: Add support for finding vCPU for given MPIDR
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
12. **[02-27 16:56]** [kvmtool PATCH v6 11/17] arm64: Add skeleton implementation for PSCI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
13. **[02-27 16:56]** [kvmtool PATCH v6 12/17] arm64: psci: Implement CPU_SUSPEND
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
14. **[02-27 16:56]** [kvmtool PATCH v6 13/17] arm64: psci: Implement CPU_ON
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
15. **[02-27 16:56]** [kvmtool PATCH v6 14/17] arm64: psci: Implement AFFINITY_INFO
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
16. **[02-27 16:56]** [kvmtool PATCH v6 15/17] arm64: psci: Implement MIGRATE_INFO_TYPE
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
17. **[02-27 16:56]** [kvmtool PATCH v6 16/17] arm64: psci: Implement SYSTEM_{OFF,RESET}
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
18. **[02-27 16:56]** [kvmtool PATCH v6 17/17] arm64: smccc: Start sending PSCI to userspace
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 2: pKVM breakage in mainline on n1sdp

**📧 邮件数**: 8 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 20 Feb 2026 19:08:59 +0000

#### 🤖 AI 总结

在本邮件讨论中，主要关注的是在 N1SDP 平台上运行 pKVM 模式时出现的问题。最初的 patch 是由 Fuad Tabba 提出的，旨在解决在主线内核中运行 kvm-unit-tests 时出现的错误，具体表现为在执行某些测试时出现警告信息。

历史讨论中，参与者们探讨了问题的根源，Marc Zyngier 提出需要明确内核版本信息，以便更好地定位问题。经过几轮讨论，发现可能是由于构建系统的问题导致版本信息显示不准确，Mark Brown 和 Mark Rutland 进一步分析了构建过程，认为可能是构建时未能正确获取 git 描述信息。

在本周的新讨论中，Mark Rutland 和 Mark Brown 继续关注构建系统的问题，确认当前的构建方式可能导致版本信息的误报。Fuad Tabba 对此表示感谢，并确认了问题的可能性，进一步推动了对该 patch 的修复工作。整体来看，讨论集中在明确问题来源和确认修复方案上，参与者们积极协作，推动了问题的解决进程。

#### 📝 邮件列表

1. **[02-20 19:08]** pKVM breakage in mainline on n1sdp
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[02-21 10:33]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-21 10:38]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-21 13:42]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[02-22 08:34]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[02-23 10:05]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Mark Rutland <mark.rutland@arm.com>
7. **[02-23 14:27]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[02-23 16:26]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Mark Brown <broonie@kernel.org>

---

